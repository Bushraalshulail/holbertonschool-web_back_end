import { readDatabase } from '../utils.js';

export default class StudentsController {
  static async getAllStudents(req, res) {
    const file = process.argv[2];
    try {
      const data = await readDatabase(file);
      let response = 'This is the list of our students\n';
      Object.keys(data)
        .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))
        .forEach((field) => {
          response += `Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}\n`;
        });
      res.status(200).send(response.trim());
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const file = process.argv[2];
    const major = req.params.major;
    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }
    try {
      const data = await readDatabase(file);
      res.status(200).send(`List: ${data[major].join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}
