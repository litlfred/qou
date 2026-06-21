#!/usr/bin/env python3
"""
The λ₊^ℓ "open-transfer dominant-channel" reading of the Aufbau order is NOT an
un-derived assumption — it is the SCALAR ACTION on the symmetric Wedderburn block,
already proved sorry-free in Lean (`QOU.Molecular.symmetric_block_domain_weight`,
content block `prop:symmetric-block-domain-weight`).

This script makes the channel identification rigorous and contrasts the three
candidate angular weights, resolving the factor-of-2 (q^ℓ vs q^{2ℓ}) that the
earlier aufbau probes left open:

  KEY IDENTITY.  The photon–electron transfer matrix
      T_γe = [[q − q⁻¹, 1], [1, 0]]
  has eigenvalues EXACTLY {q, −q⁻¹} — identical to the Iwahori–Hecke generator
  eigenvalues from (σ − q)(σ + q⁻¹) = 0.  So T_γe IS a Hecke generator σ_i, its
  Perron (dominant) eigenvalue is λ₊ = q = the SYMMETRIC-channel eigenvalue, and
  λ₋ = −q⁻¹ = the ANTISYMMETRIC-channel eigenvalue.

  CHANNELS (weight of a length-L word / spin-ℓ angular object):
    (sym)   symmetric (trivial) block:  σ_i ↦ q (SCALAR) ⇒ word weight = q^L = λ₊^L
            — proved: symmetric_block_domain_weight (Lean, sorry-free).
    (anti)  antisymmetric (sign) block: σ_i ↦ −q⁻¹       ⇒ (−q⁻¹)^L = λ₋^L.
    (qdim)  q-DIMENSION (TRACE over the full (2ℓ+1)-dim irrep):
            [2ℓ+1]_q = (q^{2ℓ+1} − q^{−(2ℓ+1)})/(q − q⁻¹) ~ q^{2ℓ}.

  WHY λ₊^ℓ AND NOT λ₊^{2ℓ}: the electron domain's energy is the SCALAR ACTION on
  the 1-dim symmetric block (the block the C_nv assembly projector selects), which
  is q^L exactly — NOT the q-DIMENSION (a TRACE over the (2ℓ+1)-dim rep, ~q^{2ℓ}).
  These are different objects; the physical weight is the scalar action. That is
  the factor-of-2 resolution the q-dim / √-q-dim probes were missing.

  ⚠ DO NOT ASSUME ONLY SCALAR CHANNELS (owner correction, 2026-06-21).  The
  q^ℓ = λ₊^ℓ reading uses the SCALAR (trivial, 1-dim) block, where σ_i ↦ q. But
  angular momentum ℓ intrinsically lives in the NON-scalar (2ℓ+1)-dim irrep V_ℓ,
  where σ_i is a MATRIX and the natural objects are:
    • the WEIGHTS of V_ℓ: q^{2m}, m=−ℓ..ℓ   (no weight equals q^ℓ — would need
      half-integer m=ℓ/2)
    • the HIGHEST WEIGHT: q^{2ℓ}             (a=+2, overshoot)
    • the TRACE (q-dimension): [2ℓ+1]_q ~ q^{2ℓ}  (a=+2, overshoot)
  EVERY natural object on the genuine non-scalar angular rep gives q^{2ℓ}
  (a=+2). q^ℓ (a=+1) is obtainable ONLY by (i) projecting onto the scalar block
  AND (ii) equating word-length with ℓ. Both are assumptions — and assuming them
  IS assuming Madelung. So the scalar shortcut is LOAD-BEARING for a=+1.

  HONEST status:
    DERIVED  λ₊ = q is the Perron eigenvalue on EVERY block (σ_i has eigenvalues
             {q, −q⁻¹} in every rep — quadratic Hecke relation); T_γe IS a Hecke
             generator (eigenvalue identity below). On the SCALAR block, a length-L
             word weighs q^L (symmetric_block_domain_weight, Lean sorry-free).
    OPEN     the ordering. a=+1 is NOT derived: the genuine non-scalar angular rep
             V_ℓ gives a=+2 (overshoot) by weights, highest weight, AND trace;
             q^ℓ needs the unjustified scalar projection. NOT accepted as a
             semi-empirical input (owner STRICT) — it is the open derivation
             target, now correctly framed as "why would the angular domain be the
             scalar-block projection (q^ℓ) and not the non-scalar V_ℓ action
             (q^{2ℓ})?", tied to conj:palindromicity-orbital-type.
"""
from __future__ import annotations
import sympy as sp

LET = "spdfghi"
NMAX = 6
ORB = [(n, l) for n in range(1, NMAX + 1) for l in range(n)]


def aufbau_reference():
    return sorted(ORB, key=lambda o: (o[0] + o[1], o[0]))


def order_by(key):
    return sorted(ORB, key=lambda o: (key(*o), o[0]))


def fmt(seq, k=12):
    return " ".join(f"{n}{LET[l]}" for n, l in seq[:k])


def main() -> int:
    q = sp.symbols("q", positive=True)

    # ── 1. Eigenvalue identity: T_γe eigenvalues == Hecke eigenvalues {q, −q⁻¹} ──
    T = sp.Matrix([[q - 1 / q, 1], [1, 0]])
    det = sp.simplify(T.det())
    eig = {sp.simplify(e): m for e, m in T.eigenvals().items()}
    hecke_eigs = {q, sp.simplify(-1 / q)}
    # discriminant (q − q⁻¹)² + 4 = (q + q⁻¹)²  ⇒ clean ± split
    disc = sp.simplify((q - 1 / q) ** 2 + 4 - (q + 1 / q) ** 2)
    print("  THE λ₊ = q SYMMETRIC-CHANNEL IDENTITY (sympy, exact)")
    print(f"    T_γe = [[q−q⁻¹, 1],[1, 0]],   det = {det}   (= −1)")
    print(f"    discriminant (q−q⁻¹)²+4 − (q+q⁻¹)² = {disc}   (⇒ √ = q+q⁻¹, exact)")
    print(f"    T_γe eigenvalues = {set(map(str, eig))}")
    print(f"    Hecke eigenvalues {{q, −q⁻¹}} from (σ−q)(σ+q⁻¹)=0 = {set(map(str, hecke_eigs))}")
    match = (set(map(sp.simplify, eig)) == set(map(sp.simplify, hecke_eigs)))
    print(f"    ⇒ identical: {match}   →  T_γe IS a Hecke generator σ_i")
    print(f"    λ₊ = q  (Perron, dominant for q>1) = SYMMETRIC eigenvalue")
    print(f"    λ₋ = −q⁻¹ (sub-dominant)           = ANTISYMMETRIC eigenvalue\n")

    # ── 2. The three channels as q-powers (leading behaviour) ──────────────────
    print("  THREE ANGULAR CHANNELS (weight of a length-L / spin-ℓ object)")
    def qdim(m):  # quantum dimension of the m-dim irrep, m = 2ℓ+1
        return sp.simplify((q ** m - q ** (-m)) / (q - 1 / q))
    for l in range(4):
        m = 2 * l + 1
        sym = q ** l                    # symmetric-block scalar action  (λ₊^ℓ)
        anti = sp.simplify((-1 / q) ** l)  # antisymmetric                (λ₋^ℓ)
        qd = qdim(m)                    # q-dimension (TRACE), ~ q^{2ℓ}
        print(f"    ℓ={l} (dim {m}):  sym q^ℓ={sp.nsimplify(sym)}   "
              f"anti (−q⁻¹)^ℓ={anti}   qdim[{m}]_q={qd}  (~q^{{{2*l}}})")
    print()

    # ── 3. Fill-order from each channel's q-EXPONENT key ───────────────────────
    # radial n always enters as n symmetric steps (q^n). angular ℓ:
    ref = aufbau_reference()
    print("  FILL ORDER from each channel (radial n always q^n; angular ℓ varies)")
    channels = [
        ("(sym)  λ₊^ℓ = q^ℓ   symmetric-block scalar  K=n+ℓ  a=+1", lambda n, l: n + l),
        ("(qdim) q^{2ℓ}        q-DIMENSION (trace)     K=n+2ℓ a=+2", lambda n, l: n + 2 * l),
        ("(anti) (−q⁻¹)^ℓ via ratio                    K=n−2ℓ a=−2", lambda n, l: n - 2 * l),
    ]
    for label, key in channels:
        seq = order_by(key)
        ok = (seq == ref)
        div = next((i for i in range(min(len(seq), len(ref))) if seq[i] != ref[i]), None)
        tag = "MATCHES Aufbau ✓" if ok else f"diverges #{div} ({fmt([seq[div]],1)} vs {fmt([ref[div]],1)})"
        print(f"    {label}\n        {fmt(seq)}  → {tag}")
    print()

    # ── 4. NON-SCALAR angular rep V_ℓ — do NOT assume only scalar channels ──────
    print("  NON-SCALAR ANGULAR REP V_ℓ (dim 2ℓ+1) — every natural object → q^{2ℓ}")
    for l in range(4):
        weights = [sp.simplify(q ** (2 * k)) for k in range(-l, l + 1)]
        hw = sp.simplify(q ** (2 * l))
        print(f"    ℓ={l}: weights {[str(w) for w in weights]}  "
              f"highest-wt {hw} (~q^{{{2*l}}})  trace [{2*l+1}]_q (~q^{{{2*l}}})  → a=+2")
    # is q^ℓ a weight of V_ℓ?  need 2m=ℓ ⇒ m=ℓ/2 (half-integer for odd ℓ)
    print("    q^ℓ is NOT a weight/h.w./trace of V_ℓ (needs half-integer m=ℓ/2).")
    print("    ⇒ q^ℓ requires the SCALAR (trivial) block + word-length=ℓ — assumed.\n")

    print("### Verdict (honest, post owner 'don't assume only scalar channels')")
    print("  • DERIVED: λ₊ = q is the Perron eigenvalue on EVERY block (σ_i eigs")
    print("    {q,−q⁻¹} in every rep); T_γe IS a Hecke generator (identity above).")
    print("    On the SCALAR block a length-L word weighs q^L (Lean sorry-free,")
    print("    symmetric_block_domain_weight).")
    print("  • NOT DERIVED: a=+1. The genuine NON-scalar angular rep V_ℓ gives")
    print("    a=+2 (overshoot) by weights, highest weight, AND trace. q^ℓ (a=+1)")
    print("    needs the SCALAR projection + word-length=ℓ — both assumptions, and")
    print("    assuming them IS assuming Madelung. The scalar shortcut is")
    print("    LOAD-BEARING; without it everything overshoots.")
    print("  • OPEN (NOT accepted, owner STRICT): the ordering. Correct framing —")
    print("    'why would the angular domain be the scalar-block projection (q^ℓ)")
    print("    and not the non-scalar V_ℓ action (q^{2ℓ})?' — tied to")
    print("    conj:palindromicity-orbital-type (ℓ = ½·palindromic-defect).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
