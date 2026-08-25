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
