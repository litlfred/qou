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

## The Phi_1 localisation is NOT established either — same error, one level down

atom_gen_chains(Z, N) returns EXACTLY TWO chains (g0, g1), for generators sigma_0
and sigma_1, for every (Z, N). It accumulates every nucleon's crossings into
those two. Read the body: the returns are unconditional.

thm:wedderburn-mass-formula sums over the generators i of the atomic braid
A in H_{A+Z}(q). That algebra has A+Z-1 generators:

    H-1  (A=1, Z=1)  H_2  -> 1 generator      atom_gen_chains gives 2
    D    (A=2, Z=1)  H_3  -> 2 generators                          2
    T    (A=3, Z=1)  H_4  -> 3 generators                          2
    4He  (A=4, Z=2)  H_6  -> 5 generators                          2

So my Phi_1 is a sum of exactly TWO logs regardless of A, while the chains
inside them grow. That is trivially non-extensive — and "Phi_1 is not extensive"
was precisely the defect I reported. The finding may be an artifact of the input,
not a property of the formula.

Worse, it is the SAME MISTAKE AS THE RETRACTION, one level down. atom_gen_chains
is documented as feeding atom_V_full for "the mass-tower formula" — it is built
for the TOWER construction, not for the Phi formula. I substituted a helper from
a neighbouring construction because it had a plausible name and the right
arity-ish shape, exactly as I earlier substituted nucleon chains into an atomic
formula.

## What this leaves standing

- The RETRACTION stands. It rests on the formula's own algebra (m_n - m_p is an
  input) and on nucleon_gen_chains being quark-level. Neither depends on how
  M_i is built.
- The alpha* EXCISION stands. Independent ground entirely.
- Phi_3 = w*ln q with INTEGER w survives as algebra ABOUT THE CHAINS GIVEN
  (4, 6, 6, 12, 12) — but whether those are the formula's chains is exactly
  what is now in doubt.
- The per-term decomposition, the "Phi_1 flips sign", the "Phi_2 well-behaved",
  and the chirality magnitude bound are ALL CONDITIONAL on the input being
  right, and it probably is not. Do not cite them.

## What is actually needed

A verified constructor for the formula's M_i: for generator i, the 2x2 transfer
matrix from chaining the crossing matrices of all strands j > i, over the atomic
braid in H_{A+Z}(q), giving A+Z-1 of them. I did not find one and did not write
one. Until that exists, no number computed from Phi_1/Phi_2/Phi_3 on atomic
braids should be trusted, including mine.

STOPPING HERE rather than building further on an unverified input. Three
inference layers in this session rested on a substituted object; two are already
retracted.

## Read the rest of the spec — the formula states its own domain, and I had not

wedderburn-mass-formula.md continues past the part I was working from:

  "For n >= 4, the Hecke algebra has additional irreducible representations
   (one per partition of n), producing ADDITIONAL INVARIANTS NOT CAPTURED BY
   THE 2x2 TRANSFER MATRIX. ... The mass functional uses the three extremal
   invariants as the LEADING-ORDER formula; the full partition sum gives the
   exact Markov trace."

So the three-Phi formula is explicitly LEADING-ORDER, exact only while the three
extremal blocks (sym, std, alt) exhaust the partitions. With n = A + Z strands:

    atom   n   p(n)  extremal  missing   measured ratio
    H-1    2     2      3       over-specified   5e5 off
    D      3     3      3       0  EXACT         1.448  right sign
    T      4     5      3       2                -0.179 WRONG SIGN
    3He    5     7      3       4                -0.605 WRONG SIGN
    4He    6    11      3       8                -0.227 WRONG SIGN

n = 3 is the UNIQUE n where the three extremal invariants are all of them, and D
is the ONLY atom whose sign is right. The breakdown starts exactly at the n >= 4
boundary the source names. That is a much better explanation of my measurements
than "Phi_1 is defective".

CAVEAT, and it is not small: my M_i inputs are still unverified (two chains where
the formula wants A+Z-1). So this correspondence is SUGGESTIVE, not established
— two candidate explanations for the same numbers, and I cannot separate them
until the constructor exists. Recording it because it reframes what the
constructor is for: not to fix a defect, but to test the formula inside and
outside its stated domain.

## Retiring my own flag

The previous entry flagged "alpha = m_e*8G is stated for the COMMUTATIVE limit;
I assume it carries to the full formula". It does — the formula's own coefficient
list gives alpha = m_e x 8G citing prop:binding-scale-catalan, alongside
[3]_q = (q^3 - q^-3)/(q - q^-1) and h_A = q - q^-1, and states "All quantities
are derived from q_0 and m_e. The formula has zero fitted parameters." Flag
retired. Also confirms [3]_q = q^2 + 1 + q^-2 as implemented, since
(q - q^-1)(q^2 + 1 + q^-2) = q^3 - q^-3.

## Bearing on the alpha* question

canonicalization-review.md §3.1 holds that alpha* absorbs the CHIRALITY term.
The source says what is missing at n >= 4 is the NON-EXTREMAL PARTITION
INVARIANTS. Those are different objects — chirality is the alt block, which is
one of the three the formula already has. So the spec itself points at the
partition sum rather than chirality as the deficit, which is independent support
for the conclusion I reached by an invalid route and retracted. Still not proof:
the retraction stands, and this is the source's framing, not a measurement.

## TERMINUS — this converges on a documented open problem, not a defect

Followed the spec's own pointer: "the full partition sum gives the exact Markov
trace". That sum is implemented — binding_K_direct.py:

    Binding(K) = m_e * sum_lambda y_lambda(q) * chi^lambda(beta_K) * Delta_lambda(K)

It runs, and emits NO binding prediction for any atom. Every row is
status = delta_lambda_value_present, carrying |tr_M| and B_codata and nothing
else. Its own comment says why:

  "Proved per-partition VALUE present; binding NOT computable from it alone
   (needs y_lambda*chi^lambda + the open extensive magnitude term). Emit the raw
   Sigma Delta_lambda as a labelled DIAGNOSTIC only — never a binding prediction
   (anti-laundering)."

That is the Delta_lambda many-body MAGNITUDE — AGENTS.md's Track A blocker. The
per-partition value is proved (signed Springer dimension, sorry-free, PR #4580);
the extensive term is open, and six ansaetze have already failed on the deuteron.

## So the chain closes

  1. "wrong-sign parameter-free p-n splitting"
       -> my test was invalid: correction vs a leading term the formula CONSUMES,
          and quark-level chains in an atomic formula.            RETRACTED
  2. -> "Phi_1 is not extensive"
       -> my input was invalid: two chains where the formula wants A+Z-1.
                                                                  RETRACTED
  3. -> the formula is EXPLICITLY leading-order, exact only where the three
        extremal blocks exhaust the partitions, i.e. n = 3 alone. D (n=3) is the
        only atom whose sign is right.
  4. -> the exact route is the Delta_lambda partition sum,
  5. -> which deliberately emits nothing, because the many-body magnitude is a
        known open problem.

CONCLUSION. The wrong sign at A >= 3 is NOT a defect to fix. It is a
leading-order formula evaluated outside its stated domain, and the exact
replacement is blocked on the documented Delta_lambda magnitude gap. Nothing
here is new mathematics; what is new is the route in, and two of my own claims
retracted along the way.

DO NOT build the M_i constructor as a research project. It would only re-measure
a leading-order formula whose limits the source already states. If it is built
at all, build it as a TEST: D (n = 3) should come out exact, not 45 % high. That
is a falsifiable check on the implementation, not a path to the binding.

AND DO NOT propose a seventh Delta_lambda ansatz. AGENTS.md names that
explicitly, and arriving here by a fresh route is not a licence to retry it.
