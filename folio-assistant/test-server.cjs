const http = require('http');
const fs = require('fs');
const path = require('path');
const server = http.createServer((req, res) => {
  req.on('error', () => {});
  res.on('error', () => {});
  let urlPath = req.url.split('?')[0];
  if (urlPath === '/') urlPath = '/index.html';
  const filePath = path.join(__dirname, urlPath);
  fs.readFile(filePath, (err, data) => {
    if (err) { 
      if (!res.headersSent) { res.writeHead(404); res.end('404'); }
    } else { 
      if (!res.headersSent) {
        if (urlPath.endsWith('.js')) res.setHeader('Content-Type', 'text/javascript');
        if (urlPath.endsWith('.css')) res.setHeader('Content-Type', 'text/css');
        if (urlPath.endsWith('.html')) res.setHeader('Content-Type', 'text/html');
        res.writeHead(200); res.end(data); 
      }
    }
  });
});
server.on('error', (err) => console.error('Server error:', err));
process.on('uncaughtException', (err) => console.error('Uncaught:', err));
server.listen(8080, () => console.log('Listening on 8080'));
