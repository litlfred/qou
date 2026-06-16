**Definition** (:defterm[Markov-axiom recursive ascent]{#markov-axiom-recursive-ascent}).
Given a braid $\beta \in B_n$ with Hecke representative
$T_w \in H_n(q)$ in Gröbner–Shirshov normal form, the *recursive
ascent* algorithm evaluates the canonical Jones–Markov trace
$\mathrm{tr}_M^{(n)}(T_w) \in \mathbb{Z}[q^{1/2}, q^{-1/2}]$ by

1. **Eliminate inverse generators.** Whenever an
   $\sigma_i^{-1}$ factor appears, expand
   $\sigma_i^{-1} = \sigma_i - (q - q^{-1})$
   (the Hecke-relation identity for the inverse), so that the
   reduced word contains only positive generators.
2. **Peel the top generator.** Express
   $T_w = T_{w'} \cdot \sigma_{n-1}$ with
   $T_{w'} \in H_{n-1}(q)$ via Garside / Gröbner–Shirshov
   normalisation; the
   ([Markov pair identity](#prop:markov-pair-z2))
   gives
   $\mathrm{tr}_M^{(n)}(T_w) = z \cdot \mathrm{tr}_M^{(n-1)}(T_{w'})$
   where $z = 1 / (q^{1/2} + q^{-1/2})$.  (No inverse factor
   is ever peeled; inverses were eliminated in step 1.)
3. **Branch on the Hecke quadratic.** Whenever a $\sigma_i^2$
   factor appears, expand
   $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$
   into two recursive sub-traces and combine.
4. **Recurse** on $T_{w'}$ at level $n - 1$ until the chain
   $H_n \supset H_{n-1} \supset \cdots \supset H_1$ terminates
   at the base case $\mathrm{tr}_M^{(1)}(\mathbf{1}) = 1$.

**Why this matters.** The naive Hoefsmit per-Wedderburn-block path
materialises symbolic matrices of dimension up to $\dim_\lambda \leq 462$
for every partition $\lambda \vdash 3A$ and multiplies along the
braid word — for $A \geq 4$ this is computationally infeasible
(${\sim} 30$ minutes per atom).  Recursive ascent never
materialises a matrix representation: the cost is bounded by the
braid length and the depth of the Hecke-quadratic branching tree.

The production implementation
(`computations/markov/markov_peel.py`) completes
$\mathfrak{m}({}^{4}\mathrm{He})$ end-to-end in ~60 s and
$\mathfrak{m}({}^{6}\mathrm{Li})$ within minutes, with all
$A \leq 3$ atoms cross-checked against the Hoefsmit + Wenzl
bridge witness (`atomic-tr-m-mpfr-50dps.witness.json`) to within
$\sim 4 \cdot 10^{-16}$.  The witness file
`markov-peel-atomic-tr-m.witness.json` records the production
results from $\mathfrak{p}, \mathfrak{n}$ through ${}^{6}\mathrm{Li}$.

**Lean status.**  The Lean module `QOU.Interactions.MarkovPeel`
declares the abstract `MarkovTrace` typeclass encoding the three
defining axioms (M1 cyclicity, M2 Markov peel, M3 unit), states
the reference identity
([Markov pair identity](#prop:markov-pair-z2)), and stubs the
recursive evaluator as a `noncomputable` declaration.  The body
of `markov_peel` and the proof of `markov_pair_z2` are open
work items
([#508](https://github.com/litlfred/qou/issues/508) Phase 6);
the Python production path supplies the computational witness in
the meantime.

**Scope of this definition.**  The recursive-ascent algorithm
covers Term 1 of the
([six-term mass formula](#thm:six-term-mass-formula-complete))
directly, and reaches Terms 4, 5, 6 via specialised inputs
(the Frobenius co-Casimir element, braid-mirror products, and
residues at primitive roots of unity respectively).  Terms 2, 3
are reachable through the
([$\Phi_q$ trace-series remark](#rem:phi-q-resums-trace-series))
via Kähler-lift differentiation or series truncation; the closed
$\Phi_q$ form remains the production fast path for those terms.
