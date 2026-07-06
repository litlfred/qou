import re

with open("content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas.lean", "r") as f:
    text = f.read()

# Remove the prediction fields from the AtlasEntry structure
text = re.sub(r'\s*m_pred_MeV\s*:\s*ℝ.*?\n', '\n', text)
text = re.sub(r'\s*m_AME_MeV\s*:\s*ℝ.*?\n', '\n', text)
text = re.sub(r'\s*err_pct\s*:\s*ℝ.*?\n', '\n', text)
text = re.sub(r'\s*err_ppb\s*:\s*ℝ.*?\n', '\n', text)

# Also remove the 3. The mass-formula prediction B_pred... from the top comment
text = text.replace("3. The mass-formula prediction B_pred = ρ · m_e · Vol_hyp(K).\n  4. The AME residual.", "3. The formal Vol_hyp.")

# Update the Methodology inductive enum
new_methodology = """inductive Methodology where
  | principledDerivation             -- explicit σ-word → closure → hp Vol
  | principledGbNf                   -- trivial-NF (unknot, disjoint unknots)
"""
text = re.sub(r'inductive Methodology where.*?\| deprecatedVolumeMatch.*?$', new_methodology, text, flags=re.MULTILINE|re.DOTALL)

with open("content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas.lean", "w") as f:
    f.write(text)
