---
# qou-r1yj
title: Lift the (T,S) grading into the 3-strands-per-nucleon construction
status: completed
type: task
priority: normal
created_at: 2026-09-02T20:52:19Z
updated_at: 2026-09-02T21:04:58Z
---


RESOLVED 2026-09-01 -- computations/probes/lifting_the_isospin_grading_to_six_strands_probe.py,
6/6. Discharges qou-m896's own caveat. MIXED answer: the cap MOVES for the first
time in this arc, and the argument that earned it does not survive.

THE EXCHANGE OPERATOR. At three strands per nucleon, exchanging two nucleons is
a BLOCK SWAP of {0,1,2} with {3,4,5} -- the braid (s3 s2 s1)(s4 s3 s2)(s5 s4 s3),
permutation [3,4,5,0,1,2] verified before use -- not a transposition.

ITS SPECTRUM IS NOT TWO EIGENVALUES. Across the four live H_6 blocks every
eigenvalue is EXACTLY +-q^k (asserted, not eyeballed):

    -q^-3  = -0.731233708    L = +3 log q   x1   (3,3)
    +q^-1  = +0.900918284    L = +1 log q   x1   (4,2)
    +-q^2  = +-1.232052454   L = -2 log q   x4   (4,2)
    +-q^3  = +-1.367551837   L = -3 log q   x5   (3,3) (5,1)
    +-q^5  = +-1.684895597   L = -5 log q   x4   (4,2)
    +-q^6  = +-1.870198027   L = -6 log q   x4   (5,1)
    +q^9   = +2.557592747    L = -9 log q   x1   (6,)

Seven distinct magnitudes, exponents {-3,-1,2,3,5,6,9}, every L an integer
multiple of log q spanning -9..+3. The n=2 structure -- two eigenvalues q and
-1/q with product -1 -- DOES NOT LIFT.

THE CAP RISES FROM 1 TO EXACTLY 3/2. Bound channels have L/log q in {3,1},
unbound in {-2,-3,-5,-6,-9}, so best |L_bound|/|L_unbound| = 3/2, attained by
L=+3 log q (from -q^-3) against L=-2 log q (from +-q^2). The det T = -1
degeneracy does NOT govern the six-strand level. THIS IS THE FIRST THING IN THE
ARC TO MOVE THE CAP AT ALL -- every convention, crossing count and Wenzl level
left it at exactly 1.

BUT IT STILL MISSES BOTH TARGETS:
    QCD colour 3bar/6      needs 2       short by 1.3333x
    nuclear deuteron/1S0   needs 33.7055 short by 22.4703x
Worth knowing WHICH it nearly reaches: the quark target, not the nuclear one.

AND THE IDENTIFICATION STOPS BEING FORCED. At n=2, Pauli forced it: T=1
symmetric, T=0 antisymmetric, and the algebra had exactly those two blocks. Here
exchange parity is NOT locked to magnitude -- q^2, q^3, q^5, q^6 each carry BOTH
signs -- so the two labels no longer pick out two channels with two values. The
only magnitudes carrying a single parity are:
    -q^-3  antisymmetric only  L = +3 log q  BOUND
    +q^-1  symmetric only      L = +1 log q  BOUND
    +q^9   symmetric only      L = -9 log q  unbound
The two pure-parity BOUND channels are ONE OF EACH PARITY, so reading T=1 as the
pure symmetric channel gives a BOUND T=1 -- exactly the failure qou-m896 fixed
at n=2. Recovering the sign pattern at six strands requires choosing an unbound
channel BY HAND, and nothing forces which.

WHAT THIS MEANS FOR qou-m896: its result stands where it was stated (n=2
interface) and is not overturned. Its caveat is discharged with a negative
answer: the grading does not lift cleanly. Both facts should be quoted together,
because the n=2 argument's force came from the identification being
Pauli-forced, and that is precisely what does not survive.

CAVEATS: 3/2 is an upper bound over the block-swap spectrum, NOT a derived
physical ratio -- which pair a physical T=0/T=1 split would use is exactly what
A6 shows is no longer forced. Only the EXCHANGE OPERATOR is lifted: no nucleon
internal words, no production bond, no binding energy recomputed. A full lift
would place the (T,S) grading inside the atom word itself, still untested.
