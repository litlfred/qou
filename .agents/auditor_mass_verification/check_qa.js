const fs = require('fs');

const files = [
  "alpha-shift-torus-knot.qa.json",
  "gb-depth-period-correspondence.qa.json",
  "knot-indexed-convolution-grid.qa.json",
  "lr-coefficient-hecke.qa.json",
  "pentagon-uv-commutation.qa.json",
  "residue-at-root.qa.json",
  "alpha-k-derivation-procedure.qa.json",
  "atom-knot-mass-derivation.qa.json"
];

const baseDir = "/home/litlfred/space_cats/qou/content/quantum-observable-universe/mass-theory/";

files.forEach(file => {
  const path = baseDir + file;
  if (!fs.existsSync(path)) {
    console.log(`${file}: NOT FOUND`);
    return;
  }
  const data = JSON.parse(fs.readFileSync(path, 'utf8'));
  console.log(`=== ${file} ===`);
  const check = (criterion) => {
    const entries = data.criteria[criterion] || [];
    if (entries.length === 0) {
      console.log(`  ${criterion}: NO ENTRIES`);
      return;
    }
    const last = entries[entries.length - 1];
    console.log(`  ${criterion}: result=${last.result}, score=${last.score ? last.score.value : 'none'}, reviewer=${last.reviewer.id}`);
  };
  check('proof-statement-integrity');
  check('proof-rater-goal-plausibility');
});
