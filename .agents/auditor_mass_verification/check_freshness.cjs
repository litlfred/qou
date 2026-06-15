const fs = require('fs');
const crypto = require('crypto');

function hashFile(path) {
  if (!fs.existsSync(path)) return undefined;
  const buf = fs.readFileSync(path);
  return crypto.createHash("sha256").update(buf).digest("hex").slice(0, 12);
}

const files = [
  "alpha-shift-torus-knot",
  "gb-depth-period-correspondence",
  "knot-indexed-convolution-grid",
  "lr-coefficient-hecke",
  "pentagon-uv-commutation",
  "residue-at-root",
  "alpha-k-derivation-procedure",
  "atom-knot-mass-derivation"
];

const baseDir = "/home/litlfred/space_cats/qou/content/quantum-observable-universe/mass-theory/";

files.forEach(name => {
  const mdPath = baseDir + name + ".md";
  const tsPath = baseDir + name + ".ts";
  const leanPath = baseDir + name + ".lean";
  const qaPath = baseDir + name + ".qa.json";

  const actualHashes = {};
  const hMd = hashFile(mdPath);
  if (hMd) actualHashes.md = hMd;
  const hTs = hashFile(tsPath);
  if (hTs) actualHashes.ts = hTs;
  const hLean = hashFile(leanPath);
  if (hLean) actualHashes.lean = hLean;

  if (!fs.existsSync(qaPath)) {
    console.log(`${name}: QA FILE NOT FOUND`);
    return;
  }

  const data = JSON.parse(fs.readFileSync(qaPath, 'utf8'));
  
  // Check if source_hashes matches actual hashes
  const sourceHashes = data.source_hashes || {};
  let hashesMatch = true;
  for (const k of ['md', 'ts', 'lean']) {
    if (actualHashes[k] !== sourceHashes[k]) {
      hashesMatch = false;
    }
  }

  console.log(`=== ${name} ===`);
  console.log(`  File hashes match source_hashes: ${hashesMatch ? 'YES' : 'NO'}`);
  if (!hashesMatch) {
    console.log(`    Actual: ${JSON.stringify(actualHashes)}`);
    console.log(`    Source: ${JSON.stringify(sourceHashes)}`);
  }

  const check = (criterion) => {
    const entries = data.criteria[criterion] || [];
    if (entries.length === 0) {
      console.log(`    ${criterion}: NO ENTRIES`);
      return;
    }
    const last = entries[entries.length - 1];
    
    // Check if last entry's field_hash matches actual hashes (for keys present in field_hash)
    let entryFresh = true;
    const fh = last.field_hash || {};
    for (const k in fh) {
      if (fh[k] !== actualHashes[k]) {
        entryFresh = false;
      }
    }
    // Also, if a file exists, it should be in field_hash if that file is a dependency
    // depends_on: ['lean'] for proof-statement-integrity, ['lean'] for goal-plausibility
    // In our case, the dependencies are ['lean'] (and/or md, ts)
    if (fh.lean && fh.lean !== actualHashes.lean) entryFresh = false;
    if (fh.md && fh.md !== actualHashes.md) entryFresh = false;
    if (fh.ts && fh.ts !== actualHashes.ts) entryFresh = false;

    console.log(`    ${criterion}: result=${last.result}, score=${last.score ? last.score.value : 'none'}, fresh=${entryFresh ? 'YES' : 'NO'}`);
  };

  check('proof-statement-integrity');
  check('proof-rater-goal-plausibility');
});
