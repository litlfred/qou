# Geometric `W_λ` — the modulus-identification gap, scoped (colored Lawrence–Rozansky amplitude)

**Date:** 2026-07-12 · **Axis:** s5-so3 keystone geometric `W_λ` · **Status:** the single remaining
open object, precisely located; rigorous execution **blocked this pass on source access** (arxiv/SIGMA
403 through the sandbox proxy). **No fit; nothing fabricated.**

## What is already derived (this session)

- **Value map** `d_q(λ) = [mark]_q` — via McKay `2I ↔ affine Ê₈` (irrep dims = Coxeter marks) ∘
  `A₅⊂S₅` branching. Exact at generic `q` (#3685); the two new members formalized sorry-free (#3699,
  `KeystoneMcKayValueMap.lean`). The standard-rep member `d_q((n−1,1))=[n−1]_q` is #3640.
- **Framing is a pure phase** — `d_q(λ)=[mark]_q` is real on the unit circle (`sin(mφ)/sin(φ)`, SU(2)
  character), so `θ_λ(ζ)=ζ^{c(λ)}` is a phase and the observable `W_λ(q₀)=d_{q₀}²/D²` is framing-free
  for all 7 blocks (#3703). Seifert framing pinned `f=−1` (Σ(2,3,5) = −1 surgery on the left trefoil).

## The single remaining gap

**The modulus identification:**

  `|S_{0λ}^{Σ(2,3,5)}(ζ)| = d_ζ(λ)/D(ζ)`,

i.e. that the **actual colored Lawrence–Rozansky vacuum-row amplitude** of Σ(2,3,5) (the geometric WRT
object) has modulus equal to the Hecke quantum dimension `d_ζ(λ)` derived above. #3685/#3699 supply the
**value** `d_q(λ)=[mark]_q`; what remains is the identification of that value with the **actual
geometric amplitude modulus**.

### Why the corpus does not already close it

The corpus [`keystone_colored_sigma235_wrt.py`](../../computations/probes/keystone_colored_sigma235_wrt.py)
computes the **colored false theta** `Ψ^{(α)}(q)` — the Lawrence–Zagier/Hikami closed form with the
order-5-fibre colour shift `1/5 → α/5`. That object is a **scalar** `q`-series (one number per colour
`α`), the **diagonal / closed-manifold** contraction — a **type mismatch** with the S-matrix **row**
`S_{0λ}` (correctly flagged there; no `Ψ=W_λ` asserted). The modulus identification requires the
**off-diagonal** colored amplitude — the Reshetikhin–Turaev surgery sum with the `S_{λμ}/S_{0μ}`
insertion for a `λ`-coloured Wilson line on the exceptional fibre — **not** the scalar false theta.

## The concrete plan (formalize-first; correctness-anchored)

1. **Formula (pinned in structure, exact normalization needs the source).** SU(2)_k WRT of a Seifert
   homology sphere via Lawrence–Rozansky/Hikami: a sum over `μ` weighted by `S_{0μ}^{2-n}` and the
   T-matrix Gauss sums of the three legs `(2,3,5)`; the colored insertion multiplies by `S_{λμ}/S_{0μ}`.
   Modular data at level `N=k+2`: `S_{0j}=√(2/N)·sin(π(2j+1)/N)`, `θ_j = exp(2πi(j(j+1)/2)/N·…)`.
2. **Correctness anchor.** Trivial colour (`λ=0`) must reproduce the **bare** invariant — the corpus
   Lawrence–Zagier `Ψ(1/q₀) ≈ 2.32958`
   ([`keystone-habiro-wrt-s3-2i.witness.json`](../../computations/keystone-habiro-wrt-s3-2i.witness.json)).
   Any colored-amplitude implementation must pass this before its modulus is compared to `d_ζ/D`.
3. **The check.** Compute `|S_{0λ}^{Σ(2,3,5)}(ζ)|` from the anchored amplitude at fibre roots of unity
   `ζ` and test `= d_ζ(λ)/D(ζ)` (the McKay-labelled Hecke q-dim). Zero free parameters. Either it holds
   (the geometric derivation of the vacuum-row modulus, closing the gate) or it fails quantifiably.

## Blocker this pass (honest)

The **exact off-diagonal normalization** (the leg Gauss-sum prefactors and the surgery framing
correction) needs Hikami, *On the Quantum Invariant for the Spherical Seifert Manifold*
(`math-ph/0504082`) / *Quantum Invariant, Modular Form, and Lattice Points* — both **403 through the
sandbox proxy** (arxiv PDF, ar5iv HTML, SIGMA PDF all blocked). Implementing the normalization from
partial memory would risk a wrong prefactor, and a spuriously-matching (or spuriously-failing) modulus
would be an **anti-laundering violation** (a guessed normalization passed off as a derivation). **Not
done; not fabricated.** Execute in an environment with arxiv access, against the anchor in step 2.

## Scope (STRICT — anti-laundering)

Records the precise remaining gap and plan; **derives nothing new** and wires **no** constant. Prevents
re-walking (the scalar `Ψ^{(α)}` is *not* the S-matrix row; the off-diagonal amplitude is the object).
The gate stays open at exactly this one identification. No fit.
