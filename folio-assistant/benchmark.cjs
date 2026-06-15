const fs = require('fs');
const html = fs.readFileSync('./simulators/brings_surface.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (scriptMatch) {
  let js = scriptMatch[1];
  js = js.replace(/const scene = new THREE\.Scene\(\);/, 'const scene = { add:()=>{}, remove:()=>{} };');
  js = js.replace(/const camera = new THREE\.PerspectiveCamera[\s\S]*?;/, '');
  js = js.replace(/const renderer = new THREE\.WebGLRenderer[\s\S]*?;/, '');
  js = js.replace(/const controls = new OrbitControls[\s\S]*?;/, '');
  
  js = `
    const THREE = {
      Vector3: class { constructor(x,y,z){} },
      BufferGeometry: class { setFromPoints(){ return this; } setIndex(){ return this; } computeVertexNormals(){} },
      LineBasicMaterial: class {},
      MeshStandardMaterial: class {},
      Line: class {},
      Mesh: class {}
    };
    const document = {
      getElementById: () => ({ checked: true, value: "1", style: {} }),
      querySelectorAll: () => [],
      querySelector: () => ({ classList: { add:()=>{} } }),
      addEventListener: () => {}
    };
    const window = { location: { search: "" }, innerWidth: 100, innerHeight: 100 };
    const cv = { width: 100, height: 100 };
    const ctx = { scale:()=>{}, clearRect:()=>{}, fillStyle:"", font:"", beginPath:()=>{}, moveTo:()=>{}, lineTo:()=>{}, fill:()=>{}, stroke:()=>{}, fillText:()=>{} };
  ` + js.replace(/function animate\(\) \{[\s\S]*?\}/, 'function animate(){}');
  
  js += `
    projMode = 'sp1';
    console.time('buildSurface');
    // For a single call to mimic what the browser does
    for (let i=0; i<1; i++) {
       const rmin = 0.25, rmax = 3.2, dr = 0.08, dzeta = 0.15;
       const qN = 12;
       let nR = Math.floor((rmax - rmin) / dr);
       let nAlpha = Math.floor(2 * Math.PI / dzeta);
       let b = 1.0;
       
       let count = 0;
       for (let r=0; r<=nR; r++) {
         for (let a=0; a<=nAlpha; a++) {
            point3D(rmin + r*dr, a*dzeta, b, {g1:1, g2:1, g3:1}, qN);
            count++;
         }
       }
       console.log("Total points computed:", count);
    }
    console.timeEnd('buildSurface');
  `;
  try {
    eval(js);
  } catch(e) { console.error(e); }
}
