# Pre-registration: does the QOU braid crossing carry the QCD quark–gluon colour factor?

Date 2026-11-22, branch `claude/mn-own-identity-2026-11-21`. Written and pushed before
`mn_quark_gluon_vertex_probe.py` was written or run. Disclosure: the expected values below
were derived by hand from the standard ribbon/Casimir formula while reading
`eightfold-way/sl-n-color-framing.md` and `QOU/Braiding/SlNFramingColourFactor.lean`
(sorry-free); the probe checks them on explicit Jimbo matrices.

## What the corpus already fixes (corpus-grep done; not re-derived)

- `prop:sl-n-color-framing`: with σ^sl = q^{-1/N}σ, eigenvalues on V⊗V are q^{2c_S},
  −q^{2c_A}, c_R = ½(C₂(R) − 2C_F); c_A/c_S = −2 iff N = 3; q^{-1/N} forced by trivial
  monodromy of V around Λ^N V (all of this in Lean, generic field).
- `sl-n-color-frame-scope.md`: framing applies to colour observables only, not to z or
  convention D; at N = 2 the ratio is 3, not the nuclear 33.7.
- `docs/audits/2026-11-15-quark-factor-relations-and-colour-channel.md`: level-2
  (convention D, C²) channels cannot host colour, (1³) has Wenzl weight 0 at level 2.

## Hypothesis / identification under test

H: the order-h term of log of the (framed) crossing eigenvalue on each irreducible summand
of (C³)^{⊗n} equals the one-gluon-exchange colour factor Σ_{i<j} T_i·T_j (normalisation
T(F) = ½), with C_F = 4/3.

Expected status: this is the Drinfeld–Jimbo statement R = q^{Ω}(1 + …), Ω the split
Casimir, i.e. the standard expansion. It is an identification test of a known fact, not
a QOU prediction.

## Construction (exact, sympy, q symbolic; s = q^{1/3} for the framing)

- Jimbo Ř on C^N⊗C^N: Ř(e_i⊗e_i) = q e_i⊗e_i; for i<j, Ř(e_i⊗e_j) = e_j⊗e_i,
  Ř(e_j⊗e_i) = e_i⊗e_j + (q−q⁻¹) e_j⊗e_i (the N = 2 case is the constraints' Rc).
  Check Hecke relation and braid relation on (C^N)^{⊗3}.
- n = 2: eigenvalues of q^{-1/N}Ř on Sym², Λ².
- n = 3: full twist Δ² = (σ₁σ₂)³ on (C³)^{⊗3}; it is central in the image, eigenvalue on
  isotypic component λ; framed by q^{-6/N}. Read Σ_{i<j}T_i·T_j = log(Δ²_framed)/(4 log q).
- qq̄: use V* ≅ Λ²V (sl₃). Monodromy of strand 1 around the pair (2,3):
  M = Δ²₁₂₃ (σ₂²)⁻¹ restricted to the subspace where strands 2,3 are in Λ²V; framed by
  q^{-4/N} (6 − 2 = 4 crossings). Read T_V·T_{V*} = log M/(4 log q).
- Framing forcing: monodromy of V around Λ^N V, N = 2 (on (C²)^{⊗3}) and N = 3 (on
  (C³)^{⊗4}), = q² unframed; solve c^{2N}q² = 1.
- Markov parameter from Ř: z_N = ptr_{K_{2ρ}}(Ř)/[N] for N = 2, 3.
- Expansions of log λ in h₁ = log q and in h = q − q⁻¹ (series to order h⁵).

## Predictions

(a) framed N = 3 exponents: Sym² 2/3, Λ² −4/3 (log/ log q); T·T = 1/3, −2/3; ratio −2.
    In h = q − q⁻¹ the order-h coefficient of log|λ_R| is exactly c_R, with nonzero h³
    terms (log q = asinh(h/2)). In log q the expansion is exactly linear (no higher terms).
    Unframed Hecke ratio: −1.
(b) baryon (1³): framed full twist q^{-8} ⇒ Σ T_i·T_j = −2 = −(3/2)C_F. Decuplet q^{4}
    (+1), octets q^{-2} (−½), multiplicities 10, 16, 1. qq̄ singlet: T·T̄ = −4/3 = −C_F;
    octet +1/6.
(c) forced c = q^{-1/2} (N=2), q^{-1/3} (N=3). N = 2: c_S = 1/4, c_A = −3/4, ratio −3,
    C_F = 3/4; Λ³(C²) = 0, so the three-strand singlet does not exist on (C²)^{⊗3}.
    z₂ = q³/(q²+1) (convention D), z₃ = q⁴/(q⁴+q²+1).

## Decision rule

- Any mismatch of an exact exponent with the Casimir value ⇒ report the identification as
  failed for that summand (scope a), and stop calling it reproduced.
- All match ⇒ report "the standard Drinfeld–Jimbo expansion, reproduced; nothing QOU-
  specific" unless the probe finds a fact not implied by the ribbon formula.
- On C² (the corpus nucleon model): state whether C_F = 4/3 is reachable. Expected: no —
  only the N = 2 Casimir 3/4 is, and only after a framing choice that the Hecke algebra
  does not make (it is N-independent; N enters through the representation).

## Honesty clause

No selection, no fitting: N, framing and summands are fixed above. A match is expected and
is not evidence for QOU; it shows the crossing is the standard quantum-group braiding. If
something does not match, it is reported as found. Exact arithmetic only; no float64.
