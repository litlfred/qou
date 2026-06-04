# Step 5 — concrete n=3 Markov trace in Lean (ready-to-paste)

**Companion to** [`2026-06-04-fibre-composite4-implementation-spec.md`](2026-06-04-fibre-composite4-implementation-spec.md)
**Step 5**. This delivers the Lean replacement for the `True`-marker
`MarkovTrace` class in
[`MarkovTraceOnHecke.lean`](../../content/quantum-observable-universe/lean/QOU/Machinery/MarkovTraceOnHecke.lean):
a **concrete H₃(q) Markov-trace functional** on the NF free module, with
linearity, the Hecke operator identity, and the Markov reduction proved
as lemmas — mirroring `gram.py`'s NF basis + `TR_M` exactly.

## Why a design doc and not a committed `.lean`

This branch's session ran in a web sandbox with **no Lean toolchain and
no way to install one**:

- `elan`/`lake`/`lean` are all absent (`command -v` → MISSING);
- the elan installer is network-blocked (`curl … elan-init.sh` → **HTTP
  403**);
- the Lean LSP cannot start (`lean_diagnostic_messages` →
  *"No such file or directory: 'lake'"*).

Per CLAUDE.md ("Don't iterate Lean proofs blind when the LSP is cold")
and the file-hygiene / shared-build rules, dropping **unverified**
non-trivial Lean into the `QOU` package would risk breaking
`lake build QOU` for every sibling — one unknown simp-lemma name is
enough. So the code lives here, ready to paste, instead.

## Verification status (important)

| layer | status |
|-------|--------|
| **Mathematical content** (NF tables, `TR_M`, Hecke identity, Markov reduction) | ✅ **cross-verified in Python** against `gram.py` — 200-sample randomized checks all pass (see below) |
| **Lean syntax / tactic invocations** | ⏳ **unverified** — needs a warm `lake build QOU` (sandbox block above) |

The Python cross-check (reproducible via `pyhecke`):

```text
mulσ₀/mulσ₁ tables match gram.hm:           True
Hecke σ₀²=hσ₀+1 operator identity:          True
Markov reduction trM(x·σ₁)=z·trM(x) on H₂:  True
TR_M = [1, z, z, z², z², h·z²+z]            (matches gram.TR_M)
```

The same identities are checked symbolically over ℚ(s) by
[`test_trace_formal.py`](../../tools/pyhecke/tests/test_trace_formal.py)
(`test_hecke_relation_symbolic`, `test_basis_word_traces_match_TR_M`).
So only the **Lean encoding** is open, not the math.

## The code

Paste into `MarkovTraceOnHecke.lean` (add the import; keep the existing
abstract `MarkovTrace` class for downstream consumers, or upgrade its
field per the realization theorem at the end). The NF basis order is
`[γ, σ₀, σ₁, L₊, L₋, e⁻]`, identical to `gram.NF_BASIS`.

```lean
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic

namespace QOU.Machinery.H3

variable {R : Type*} [CommRing R]

/-- Markov-Ocneanu-Wenzl weights on the GB-NF basis
`[γ, σ₀, σ₁, L₊, L₋, e⁻]` of `H₃(q)` (mirrors `gram.TR_M` /
`trace_formal.TR_M_formal`). `z` is the Markov parameter, `h = q − q⁻¹`.
Note `tr_M(e⁻) = h·z² + z` — the 2026-05-19 fix, NOT `z³`
(`docs/audits/2026-05-19-trm5-markov-bug.md`). -/
def TRM (z h : R) : Fin 6 → R := ![1, z, z, z ^ 2, z ^ 2, h * z ^ 2 + z]

/-- The **Markov trace** on the NF free module `Fin 6 → R`: the linear
functional `v ↦ ∑ᵢ vᵢ · TRMᵢ`. Replaces the `True`-marker. -/
def trM (z h : R) (v : Fin 6 → R) : R := ∑ i, v i * TRM z h i

/-- Right action of `σ₀` on the NF basis (mirrors `gram.hm(·,1,0,0)`):
`e₀↦e₁`, `e₁↦h·e₁+e₀`, `e₂↦e₃`, `e₃↦h·e₃+e₂`, `e₄↦e₅`, `e₅↦h·e₅+e₄`. -/
def mulσ₀ (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 1, v 0 + h * v 1, v 3, v 2 + h * v 3, v 5, v 4 + h * v 5]

/-- Right action of `σ₁` on the NF basis (mirrors `gram.hm(·,1,0,1)`). -/
def mulσ₁ (h : R) (v : Fin 6 → R) : Fin 6 → R :=
  ![v 2, v 4, v 0 + h * v 2, v 5, v 1 + h * v 4, v 3 + h * v 5]

/-- **(M1) Linearity** — additivity. -/
theorem trM_add (z h : R) (u v : Fin 6 → R) :
    trM z h (u + v) = trM z h u + trM z h v := by
  simp only [trM, Pi.add_apply, add_mul, Finset.sum_add_distrib]

/-- **(M1) Linearity** — homogeneity. -/
theorem trM_smul (z h c : R) (v : Fin 6 → R) :
    trM z h (c • v) = c * trM z h v := by
  simp only [trM, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  exact Finset.sum_congr rfl (fun i _ => by ring)

/-- **(M3) Hecke relation** as an operator identity: `σ₀² = h·σ₀ + 1`.
(The same statement holds for `σ₁`; copy with `mulσ₁`.) -/
theorem mulσ₀_hecke (h : R) (v : Fin 6 → R) :
    mulσ₀ h (mulσ₀ h v) = h • mulσ₀ h v + v := by
  funext i
  fin_cases i <;>
    simp [mulσ₀, Pi.add_apply, Pi.smul_apply, smul_eq_mul] <;> ring

/-- **(M3) Markov reduction** `tr(x·σ₁) = z·tr(x)` for
`x ∈ H₂ = span{γ, σ₀}` (i.e. `v 2 = v 3 = v 4 = v 5 = 0`). This is the
defining Markov property at the H₂ ↪ H₃ inclusion. -/
theorem trM_markov_σ₁ (z h : R) (v : Fin 6 → R)
    (h2 : v 2 = 0) (h3 : v 3 = 0) (h4 : v 4 = 0) (h5 : v 5 = 0) :
    trM z h (mulσ₁ h v) = z * trM z h v := by
  simp only [trM, mulσ₁, TRM, Fin.sum_univ_six,
    Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.head_cons]
  rw [h2, h3, h4, h5]; ring

/-- The concrete n=3 trace satisfies the Markov laws — it is a **real**
linear functional, no longer a `True` marker. Use this to give the
abstract `MarkovTrace` a non-trivial instance, or to discharge a
downstream obligation once Step 4 names the element. -/
theorem markovTrace_realized (z h : R) :
    (∀ u v, trM z h (u + v) = trM z h u + trM z h v) ∧
    (∀ c v, trM z h (c • v) = c * trM z h v) ∧
    (∀ v : Fin 6 → R, v 2 = 0 → v 3 = 0 → v 4 = 0 → v 5 = 0 →
       trM z h (mulσ₁ h v) = z * trM z h v) :=
  ⟨trM_add z h, trM_smul z h, trM_markov_σ₁ z h⟩

end QOU.Machinery.H3
```

## Tactic fallbacks (if a proof doesn't close first try)

The math is verified; only lemma-name plumbing for the `![…]`
(`Matrix.vecCons`) indexing can differ across Mathlib pins:

- **`mulσ₀_hecke`** — if `simp` leaves `![…] k` unreduced after
  `fin_cases i`, add `Matrix.cons_val_fin_one, Matrix.cons_val_succ` (or
  `Matrix.cons_val'`, `Fin.isValue`) to the simp set; the goal is then a
  pure `ring` identity in `v 0 … v 5, h`.
- **`trM_markov_σ₁`** — the `Fin.sum_univ_six` + `cons_val` reduction
  yields a polynomial in `v 0 … v 5, z, h`; if `cons_val_one`/`head_cons`
  aren't enough for indices 2–5, use `decide`-free
  `simp [Matrix.cons_val]` or `Fin.cons_succ`. After `rw [h2,h3,h4,h5]`,
  `ring` closes it.
- General safety net: `fin_cases i <;> simp [all the defs] <;> ring`
  evaluates everything component-wise and almost always closes these
  finite identities.

## Verify

```bash
lake build QOU            # from repo root (root Lake workspace)
# or, faster, the single module:
lake build QOU.Machinery.MarkovTraceOnHecke
```

Then `lean_diagnostic_messages` on the file should report no errors and
`lean_verify QOU.Machinery.H3.markovTrace_realized` should show no
`sorry`/extra axioms.

## Downstream payoff (gated on Step 4)

Once Step 4 names the residue-A element, the
`UniversalHabiroStructure.markov_trace_origin` field (currently `True`
in [`MmuR9V9Closure.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/MmuR9V9Closure.lean))
can be discharged using `markovTrace_realized` for that specific element,
turning the conditional closure theorem into an unconditional one — the
ultimate Step-5 goal. The concrete `trM` here is the bridge: it is the
actual functional the abstract `MarkovTrace` was a placeholder for.

## Cyclicity (follow-on, not in this drop)

Full trace cyclicity `trM(uv) = trM(vu)` needs the complete H₃
multiplication (all of `gram.hm`, both generators, both `c,d`), not just
the two single-generator actions above. It is a larger mechanical job;
the Markov reduction proved here is the defining axiom and the one the
downstream closure actually consumes. Add cyclicity when wiring the full
H₃ algebra structure (a separate Step 5b).
```

