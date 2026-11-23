# Pre-registration: per-quark charge from Q̂ and T³, all-n flip theorem, operator charge on the muon map (2026-11-22)

Owner, 2026-11-22: *"All 3. Anything from physics to guide?"* (the three options offered after §38).
Written and committed before any number below is computed.

## Part C — joint spectrum of (T³, Q̂), and one candidate per-quark charge

Weight model as §29–§38: C²⊗³, σ = Rc, V = σ₀σ₁⁻¹, Q̂ = log(V)/2πi (principal branch), T³ the
weight operator. V preserves weight, so [V, T³] = 0, so Q̂ and T³ have a joint eigenbasis.

- **C1 (joint spectrum).** Report the eight joint eigenvalue pairs (T³, Q̂) at q₀ and as q → 1.
  Prediction: (3/2, 0), (−3/2, 0), and on W_p and W_n each (±1/2, 0), (±1/2, +t), (±1/2, −t).
- **C2 (one candidate, stated with its origin).** At q = 1, t = 1/3 exactly (Lean `phase_at_one`), and
  hol = V³ has phase 3t = 1 on the (2,1) part. **Reading B:** the baryon number of the three-strand
  state is the winding of the hol eigenphase, B := 3t, i.e. B/3 = t per strand. With the
  Gell-Mann–Nishijima rule Q = T³ + B/2 *imported from physics* (it is not derived here), the
  per-strand charge is q_i = T³_i + t/2: q_u = (1 + t)/2, q_d = (t − 1)/2.
  This candidate was written down **after** seeing t(1) = 1/3, so it is a reading to be tested,
  not a derivation, and the Gell-Mann–Nishijima rule stays an import. It is the only candidate tried.
  Predictions:
  - PC2a. At q = 1: q_u = 2/3, q_d = −1/3 exactly, Q_p = 1, Q_n = 0.
  - PC2b. At q₀ the charges are not quantised: Q_p = (1 + 3t)/2 ≈ 1.00607 and Q_n = (3t − 1)/2
    ≈ +0.00607. Compared with the measured neutron charge (|Q_n| < 10⁻²¹ e), this reading **fails**
    at q₀ unless something else shifts by the same amount.
  - PC2c. Used as scalar charges in S = QPair·hol on the §35 maps: E-pot plain and K both
    positive, between 40 and 60 keV at q₀, with limit 1/8 at q = 1 (any scalar charges that reduce
    to (⅔, −⅓) at q = 1 give the 1/8). M2 diverges as q → 1.

## Part L — Lean: n − p = 0 at q = 1, for every n

At q = 1, Rc is the swap, σ⁻¹ = σ, so every braid word acts on C²⊗ⁿ as a strand permutation
matrix, and the T³ term of 𝒟 has coefficient 1 − q⁻¹ = 0. To prove, over any commutative ring:
the global flip (complement every bit) commutes with every strand permutation matrix, the matrices
commuting with it form a ring, and for such a matrix M the trace over states with w u-bits equals
the trace over states with n − w u-bits. Corollary: for hol any product of strand permutations and
𝒟 = hol − 1, tr_w(𝒟ᵏ) = tr_{n−w}(𝒟ᵏ) for all k and n. Sorry-free, standard axioms only.
Scope: this is the q = 1 statement only; the identification "Rc at q = 1 is the swap" is stated
in the docstring, not proved in the file.

## Part M — operator charge on the muon-scale map (§35 map)

M3: E_n − E_p = 2 m_μ ([3]_q!/q³)(τ_n − τ_p)(𝒟² − Q̂²·hol), with τ_p = q·tr_{W_p}/[2]³ and
τ_n = q⁻¹·tr_{W_n}/[2]³ exactly as §35. Q̂ is a matrix logarithm, so this is mpmath (60 dps) at q₀
and on a sequence q = 1 + 10⁻ᵏ, not exact sympy.
Prediction (derived in advance): Q̂²·hol has the same spectrum on both blocks to leading order,
so (τ_n − τ_p)(Q̂²·hol) ≈ (q⁻¹ − q)·2t²/8 = O(h). The map carries m_μ ∝ ℏ_q⁻², so the charge
term grows like 1/h as q → 1, positive. At q₀: M3 positive, a few MeV (order of magnitude 1–10 MeV).
So on this map the operator charge **does not** keep m_p = m_n at q = 1; the K-weighting of the map
supplies the O(h) that the pole turns into a divergence. A finite limit would refute this.

## Physics used only as comparison

CODATA m_n − m_p = 1.29333 MeV. The lattice split (Borsanyi et al. 2015, Science 347, 1452):
quark-mass part ≈ +2.52 MeV, electromagnetic part ≈ −1.00 MeV. Printed after the numbers; nothing
is selected or tuned against them. q₀ is the standing proton pin. No float64.
