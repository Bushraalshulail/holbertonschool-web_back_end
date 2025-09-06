import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) reject(err);
      else {
        const lines = data.trim().split('\n');
        const studentsByField = {};
        lines.slice(1).forEach((line) => {
          const [firstname, , , field] = line.split(',');
          if (!studentsByField[field]) studentsByField[field] = [];
          studentsByField[field].push(firstname);
        });
        resolve(studentsByField);
      }
    });
  });
}
