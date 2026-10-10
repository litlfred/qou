---
# qou-o37w
title: F4 derive R(q,x) from the BindingEigenfunctionTwoTier target, not by tuning
status: completed
type: task
priority: normal
created_at: 2026-08-26T03:37:39Z
updated_at: 2026-08-26T04:13:44Z
---

## RESULT (2026-08-26): scope-(b) exclusion + the missing structure named

**Deliverable: a NEGATIVE on a named sub-family, with the invariant cited —
plus, in the same argument, the exact statement of what is missing.**
R(q,x) was not derived and was not extracted. Nothing was tuned or fitted.

### Where the gap actually was
The 2026-07-20 audit §4 already excluded a scalar kernel on the RAW carrier
(Gevrey growth; `no_bounded_depth_first_order_kernel`, sorry-free) and §5
explicitly RE-TARGETED the conjecture at the q-Borel/Gevrey-normalized carrier
`b_n = f_n/[n]_q!`, saying "the obstruction vanishes" there and predicting
depth d = 2. That carrier provably satisfies `[m+2]_q b_{m+2} = b_{m+1} + b_m`
(`qlift_normalized_kernel_exists`, sorry-free) = the operator
`L_K = (q^2 x - 1)s^2 - (q-1)s - (q-1)` named by
conj:qdifference-kernel-prolongation-symbol. Whether THAT admits a scalar
kernel was the live question. It does not.

### The proof
A scalar kernel is a first-order right factor `s - a` of L_K, i.e. a rational
solution of `(q^2x-1)a(qx)a(x) - (q-1)a(x) - (q-1) = 0`. Cleared, the three
terms have degrees 1+2p, p+u, 2u (p = deg P, u = deg Q). The first is
odd-shaped and the third even, so 1+2p = 2u is impossible over Z; a two-line
case split gives that the maximum is attained EXACTLY ONCE for every (p,u),
and a lone top-degree term cannot cancel. No coprimality needed. Holds for
every field K and every q != 0, 1.

This parity IS the Newton-slope invariant: L_K is pure isoclinic of slope 1/2
at infinity, rank-1 q-difference modules have INTEGER slope, and slopes are
additive on sub-/quotient modules. It is the SAME invariant, with the same
citation ([rsz2013] Thm 2.2.1(i), 2.2.4), that the block's existing scope note
uses to separate K from the Stokes carrier G — pushed one step further.
Corroborated by van der Put-Reversat's E(r,d,b) normal form for pure modules
of non-integral slope d/r (irreducible when rank = r; here r = 2 = rank K),
held in-corpus at library/crmath-2011-349-19-20-1037-0/.

### Under-determination, as an exact count
With R unconstrained the kernel coefficients and body terms are in BIJECTION
(one new r_k per body order, both directions explicit). So the ansatz
constrains nothing, and "rho*A is an output of the recursion" is false unless
R is independently pinned: the recursion transfers the unknown, it does not
remove it. ALL content lives in the finiteness of the Laurent window — which
the exclusion shows the scalar form cannot have.

### What is missing (the sharp statement)
- The kernel must be a 2x2 MATRIX A(q,x) on (G, sigma G), not a scalar. The
  carrier and the depth-2 prediction both SURVIVE; "depth 2" means RANK 2.
  A rank-2 tau-image is a first-order two-component system — which is what
  "Dirac-type" already asks for, so this is the natural reading, not a patch.
- A scalar kernel returns ONLY after a degree-2 RAMIFIED base change
  (adjoining q^(1/2), x^(1/2)), where slope 1/2 becomes the integer 1. It then
  relates HALF-shifts: even and odd body orders separately. That ramification
  is the missing structure.

### One downstream claim FALSIFIED
Consequence 2 of conj:qdifference-kernel-prolongation-symbol — "determines
every body term from the deuteron base case" — is wrong by exactly one initial
condition. Rank 2 needs TWO base cases, so the n=3 three-body term is an
independent input, not an output. Converges with qou-hh9q (n=3 not forced, one
free parameter) from a different direction.

### Artifacts
- content/quantum-observable-universe/lean/QOU/Mass/BindingScalarKernelParityExclusion.lean
  sorry-free; lean-direct exit 0; #print axioms clean on all 5 declarations.
- computations/probes/binding_qdiff_scalar_kernel_parity_exclusion_probe.py
  5/5. Exact sympy over Q(q) + Fraction/mpmath 220 dps. No float64. No witness.
- Scope notes in the 3 affected .md blocks; render-latex.ts exit 0 on all three.

### Honest notes
- The Lean + probe were swept into a sibling's commit fdace2404d by a
  concurrent `git add -A` on this shared branch. Content verified byte-identical
  to my final sorry-free version; history not rewritten (shared branch).
- precision-gates.sh --changed reports RED on the raw-float64 ratchet, but with
  NEW dirty 0 / REGRESSED 0 — pre-existing baseline state, not from this change
  (this probe emits no witness).
- The da-* / expo-* sidecar criteria on the 3 blocks are at needs-agent, which
  a script cannot clear. Left honestly as such.
