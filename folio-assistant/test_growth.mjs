import fs from 'fs';
const code = fs.readFileSync('simulators/brings_surface.html', 'utf8');
const match = code.match(/function growthFactors[\s\S]*?return \{.*?\};?\s*\n\}/);
if (match) {
  eval(match[0]);
  let hasNaN = false;
  for (let r=0.12; r<=2.5; r+=0.14) {
    let gf = growthFactors(r, 18);
    for (let alpha of gf.alphaValues) {
      if (isNaN(alpha)) hasNaN = true;
    }
  }
  console.log("hasNaN:", hasNaN);
} else {
  console.log("Not found");
}
