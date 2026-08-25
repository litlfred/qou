---
# qou-q6pp
title: Why is the parameter-free p-n splitting wrong-signed? (and was my own test even valid)
status: todo
type: task
priority: normal
created_at: 2026-08-25T06:06:25Z
updated_at: 2026-08-25T06:10:19Z
---

## RETRACTION — my own committed claim was invalid, in two independent ways

ec7546ac7a (merged to main in #5622) states: 'PARAMETER-FREE p-n splitting,
nothing fitted: predicted corr(n) - corr(p) = -0.62398 MeV, CODATA m_n - m_p =
+1.29333 MeV, err -148.2 %, WRONG SIGN', and concludes that this REFUTES
canonicalization-review.md §3.1's claim that alpha* absorbs the chirality term.

**That conclusion is withdrawn.** The test could not have shown it.

### Error 1 — compared a correction against a leading term

thm:wedderburn-mass-formula is

    m(Z,N) = Z*m_p + N*m_n + Z*m_e + alpha*( Phi_1 - 2[3]_q*Phi_2 + h_A^2*Phi_3 )

so (m_n - m_p) is a LEADING term the formula CONSUMES AS INPUT, while
alpha*(Phi..) is the correction on top of it. The formula never predicts the p-n
splitting. I compared the difference of correction terms against the very
quantity the formula takes as given and called it a prediction.

### Error 2 — fed nucleon-internal chains into an atomic formula

    _PROTON_G0, _PROTON_G1 = nucleon_gen_chains(['u','u','d'])

Quark-level chains INSIDE one nucleon. The formula's M_i are drawn from the
ATOMIC braid A in H_{A+Z}(q). atom_gen_chains(Z, N) — in the same module,
which is how obvious this should have been — builds the right object, including
inter-nucleon and electron crossings.

Independent check that error 2 alone was fatal: with the nucleon chains the
correction for the proton is +0.1165 MeV against a hydrogen binding energy of
-1.36e-5 MeV. 8569x too large and the wrong sign, for a quantity that is
supposed to BE the binding.

## The correct test, and it is still a negative

alpha_gen_chains(Z,N), so alpha*(Phi..) should equal -B_AME:

    atom   Z,N     alpha*(Phi..)      -B_AME        ratio
    H-1   (1,0)      -7.39963621    -0.0000136     5e5 too large
    D     (1,1)      -3.22133812    -2.224566      1.4481  right sign, 45% high
    T     (1,2)      +1.51922867    -8.481798     -0.1791  WRONG SIGN
    3He   (2,1)      +4.67222883    -7.718043     -0.6054  WRONG SIGN
    4He   (2,2)      +6.42417246   -28.295674     -0.2270  WRONG SIGN

The correction becomes MORE POSITIVE as A grows while binding becomes more
negative — anti-correlated. And H-1, which has no nuclear binding at all, gets
-7.4 MeV where 13.6 eV is the whole answer.

So there IS a real sign problem. It is in the binding correction for A >= 3, not
in a p-n splitting the formula never claimed.

## What survives from ec7546ac7a

- The Phi_1/Phi_2/Phi_3 IMPLEMENTATION. Verified analytically; that verification
  is pure algebra and is independent of which chains are fed.
- Phi_3 = w*ln q with integer w, and Phi_2 = 2*ln(1 + h^2/4) being p/n-identical.
  Both are algebra about the chain words, and both hold for the chains named.
- alpha = m_e*8G is a DIFFERENT OBJECT from alpha*, sharing a glyph.
- **The alpha* EXCISION survives.** It rested on alpha* being a FIT (scale
  normalised on CODATA M_p, root-found on CODATA M_n, neither a CAL-1/2/3
  input). That ground is untouched by this retraction.

## What does NOT survive

The refutation of canonicalization-review.md §3.1. Whether alpha* was absorbing
the chirality term is **once again open** — my measurement did not test it.
Both docs and the commit message assert the refutation and must be corrected.


## Repair note

Two phrases in this bean were eaten by shell command substitution when it was
written: backticked (m_n - m_p) and atom_gen_chains(Z, N) were executed rather
than quoted, leaving two sentences without their subjects. Restored above.

Second time this session — the same trap also mangled a phrase in qou-l1gv.
Write bean bodies through a heredoc or a file, never as a shell argument
containing backticks.

## The defect is localised to Phi_1 — measured

Per-term decomposition with the correct atomic chains (alpha = m_e*8G):

    atom     a*Phi_1   a*(-2[3]Phi_2)   a*h^2 Phi_3     total    -B_AME
    H-1     -6.97252        -0.49542        +0.06830   -7.39964   -0.0000
    D       -2.08525        -1.23855        +0.10246   -3.22134   -2.2246
    T       +3.39845        -1.98168        +0.10246   +1.51923   -8.4818
    4He     +9.19178        -2.97252        +0.20491   +6.42417  -28.2957

1. PHI_1 IS THE WHOLE PROBLEM. It alone flips sign with A (-6.97 -> +9.19) and
   it dominates every row. Phi_1/L (L = total chain length) runs
   -0.155, -0.023, +0.025, +0.045, +0.047 for H-1/D/T/3He/4He: it is NOT
   extensive, crosses zero between D and T, and saturates near +0.047. A binding
   term must be monotone negative and grow with A. Phi_1 does the opposite.

2. PHI_2 IS WELL-BEHAVED: -0.495, -1.239, -1.982, -2.973 — monotone negative,
   roughly linear in A. Shaped like a binding term.

3. PHI_3 IS TINY AND INTEGER-QUANTISED. In units of h^2*ln q the weight w is
   EXACTLY 4, 6, 6, 12, 12 for H-1, D, T, 3He, 4He — i.e. w = 6Z once N >= 1,
   with the bare proton at 4.

## The defensible version of what I wrongly claimed

My retracted commit argued chirality cannot be what alpha* was absorbing, via an
invalid test. There IS a valid magnitude argument for the same conclusion, and
it needs no splitting test: Phi_3 contributes 0.07-0.20 MeV against deficits of
5-35 MeV. It is 1-3 % of the total and cannot close a gap two orders of
magnitude larger. That constrains MAGNITUDE only — scope-(a). It does not
exclude chirality from the formula, and it says nothing about what alpha*
absorbed in the 2-term frame, which remains open.

## Assumption that needs checking before anyone builds on this

alpha = m_e*8G is taken from cor:commutative-chirality-vanishes, which states it
for the COMMUTATIVE (q -> 1) reduction. I assumed the same alpha multiplies the
bracket in the full non-commutative formula. thm:wedderburn-mass-formula writes
"alpha" without redefining it, so this is the natural reading — but it is a
reading, not a verified identification, and every magnitude above scales
linearly with it. The SIGN results (Phi_1 flipping, Phi_2 monotone) are
alpha-independent and survive regardless.
