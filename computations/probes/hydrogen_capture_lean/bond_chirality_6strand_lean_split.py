"""Usage: python3 bond_chirality_6strand_lean_split.py bond_chirality_6strand_lean_gen.py <.../lean/QOU/BraidsAndKnots>. Run the generator per case and split into Core + one module per case + umbrella."""
import subprocess, sys, os, re
here = os.path.dirname(os.path.abspath(__file__))
gen = sys.argv[1]; outdir = sys.argv[2]   # outdir = .../QOU/BraidsAndKnots
NS = "QOU.BraidsAndKnots.BondChiralitySixStrand"
def emit(c):
    tmp = f"/tmp/claude-0/6s/_emit_{c}.lean"
    subprocess.run([sys.executable, gen, c, tmp], check=True, stdout=subprocess.DEVNULL)
    return open(tmp).read()
full = emit("GL")
head, rest = full.split("-- @@SPLIT_WORDS\n", 1)
imports_end = head.index("/-!")
doc_end = head.index("-/\n", imports_end) + 3
imports = head[:imports_end]
maindoc = head[imports_end:doc_end]
body = head[doc_end:]
coredoc = f"""/-!
# Bond chirality on six strands: shared machinery

Full-space Jimbo braiding on `(C²)^{{⊗6}}`, the restriction of any word to an invariant coordinate
subspace (`diag_word`), the four weight spaces `#0 ∈ {{1, 2, 4, 5}}`, the row-by-row action of each
generator on them, and the reduction of the functional `F(O±)` to weight-space diagonal entries.
The four values are in `BondChiralitySixStrand.Case*`; the summary is `BondChiralitySixStrand`.
-/
"""
os.makedirs(os.path.join(outdir, "BondChiralitySixStrand"), exist_ok=True)
open(os.path.join(outdir, "BondChiralitySixStrand", "Core.lean"), "w").write(
    imports + coredoc + body + f"end {NS}\n")
cases = {"GL": "CaseGLeft", "GR": "CaseGRight", "GpL": "CaseGpLeft", "GpR": "CaseGpRight"}
for c, mod in cases.items():
    t = emit(c)
    part = t.split("-- @@SPLIT_WORDS\n", 1)[1].split("-- @@SPLIT_END\n", 1)[0]
    word_doc = re.search(r"/-- (.*?)\. -/\ndef w" + c + " ", part).group(1)
    doc = f"""/-!
# Bond chirality on six strands: {word_doc}

The weight-space columns needed by `F(O₊)` and `F(O₋)` (mulVec chains, one step per letter),
then `S = F(O₊) + F(O₋)` on the full 64-dimensional space and `F(O±)` at `q = 1`.
Setup and conventions: `BondChiralitySixStrand.Core`.
-/
"""
    open(os.path.join(outdir, "BondChiralitySixStrand", mod + ".lean"), "w").write(
        f"import QOU.BraidsAndKnots.BondChiralitySixStrand.Core\n\n{doc}\nnamespace {NS}\n\nopen Matrix\n\nvariable {{R : Type*}} [Field R]\n\nset_option linter.unusedVariables false\nset_option maxHeartbeats 1000000\n\n{part}end {NS}\n")
umb = "".join(f"import QOU.BraidsAndKnots.BondChiralitySixStrand.{m}\n" for m in cases.values())
umb += "\n" + maindoc + f"""
namespace {NS}

variable {{R : Type*}} [Field R]

/-- **The four values of §43, on the full space.** `S = F(O₊) + F(O₋)` for the bond `G`
(ruled form) and the bond `G′` (non-ruled comparison arm), proton on strands `0–2` and `3–5`. -/
theorem four_values (q : R) (hq : q ≠ 0) :
    Fp64 [0, 1, 2] (word64 q wGL) + Fm64 [0, 1, 2] (word64 q wGL) = -(4 * q * (q - q⁻¹) ^ 4) ∧
    Fp64 [3, 4, 5] (word64 q wGR) + Fm64 [3, 4, 5] (word64 q wGR)
      = (3 * q ^ 2 + 1) * (q - q⁻¹) ^ 4 / q ∧
    Fp64 [0, 1, 2] (word64 q wGpL) + Fm64 [0, 1, 2] (word64 q wGpL)
      = (q ^ 2 + 1) * (3 * q ^ 4 - 2 * q ^ 2 + 1) * (q - q⁻¹) ^ 4 / q ∧
    Fp64 [3, 4, 5] (word64 q wGpR) + Fm64 [3, 4, 5] (word64 q wGpR)
      = -((3 * q ^ 2 + 1) * q ^ 3 * (q - q⁻¹) ^ 4) :=
  ⟨S_GL q hq, S_GR q hq, S_GpL q hq, S_GpR q hq⟩

/-- **`q = 1`:** in all four configurations `F(O₊) = 6` and `F(O₋) = −6`. -/
theorem at_one :
    (Fp64 [0, 1, 2] (word64 (1 : R) wGL) = 6 ∧ Fm64 [0, 1, 2] (word64 (1 : R) wGL) = -6) ∧
    (Fp64 [3, 4, 5] (word64 (1 : R) wGR) = 6 ∧ Fm64 [3, 4, 5] (word64 (1 : R) wGR) = -6) ∧
    (Fp64 [0, 1, 2] (word64 (1 : R) wGpL) = 6 ∧ Fm64 [0, 1, 2] (word64 (1 : R) wGpL) = -6) ∧
    (Fp64 [3, 4, 5] (word64 (1 : R) wGpR) = 6 ∧ Fm64 [3, 4, 5] (word64 (1 : R) wGpR) = -6) :=
  ⟨⟨Fp_GL_at_one, Fm_GL_at_one⟩, ⟨Fp_GR_at_one, Fm_GR_at_one⟩,
    ⟨Fp_GpL_at_one, Fm_GpL_at_one⟩, ⟨Fp_GpR_at_one, Fm_GpR_at_one⟩⟩

end {NS}
"""
open(os.path.join(outdir, "BondChiralitySixStrand.lean"), "w").write(umb)
print("ok")
