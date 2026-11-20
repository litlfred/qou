*Stated over $\mathbb{R}$ (archimedean regime); the combinatorial content is a finite non-negative sum.*

**Proposition (extensivity of the body-order binding).**
*Write the jet-filtration binding of [Binding many-body series equals the jet-order filtration: $B(K)=\sum_n m_e\,a_D^{(n)}$](#conj:binding-manybody-eq-jet-filtration) as*

$$
  B(A) \;=\; \sum_{n=2}^{A} \mathfrak{m}_e \, a_D^{(n)} \, w_n ,
$$

*with $\mathfrak{m}_e \geq 0$, and $a_D^{(n)} \geq 0$, $w_n \geq 0$ for every body
order $n$. Then $B$ is **monotone non-decreasing in the body-order cutoff $A$**:*

$$
  A \leq A' \;\Longrightarrow\; B(A) \leq B(A') ,
$$

*and it is **strictly increasing** whenever a new body order contributes
positively: if $\mathfrak{m}_e\, a_D^{(A+1)}\, w_{A+1} > 0$ (and $A+1 \geq 2$), then
$B(A) < B(A+1)$.*

Adding nucleon body orders can only increase binding. This is exactly the
**extensive** behaviour the *intensive* rotation-phase reading
$\theta_\lambda = \arccos(\chi^\lambda/d_\lambda)$ structurally lacked — a bounded
per-block phase cannot grow with the nucleon number $A$ (see the failed
one-parameter closure in `probe_full_theta_binding.py`). The body-order series
supplies it, because each term $\mathfrak{m}_e a_D^{(n)} w_n$ is a non-negative
contribution and the number of terms grows with $A$.

The proof is elementary — monotonicity of a finite sum of non-negative terms over
the nested index sets $\{2,\ldots,A\} \subseteq \{2,\ldots,A'\}$.

**Scope (what is *not* asserted here).** The three deeper inputs are carried as
non-negativity/positivity *hypotheses* on $a_D^{(n)}$ and $w_n$, **not** derived in
this proposition:

1. the **super-exponential magnitude** of the Seiberg–Witten period
   $a_D^{(n)} = \oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}$ — the
   *quantitative* extensive channel;
2. the **non-abelian-Stokes identity** $a_D^{(n)} = \mathrm{lw}(n-1)$ (the mean
   quantum dimension; conjectural, with residue-sum
   form `prop:sw-period-residue-sum`);
3. the per-atom **residue weight** $w_n(K)$ (the $\rho\cdot A$ scale rule, a
   $q$-difference recursion output).

What is established is the *qualitative* extensivity: given non-negative period and
weight data, the body-order binding grows with $A$.

**Status of (1)–(3) elsewhere in the corpus.** Being carried as a hypothesis *here*
is not the same as being open, and only one of the three now is. Item (2) is open:
it is axiomatised as the §3b conjecture class
`QOU.Mass.NaStokesKeystone.ProlongationPeriodMeanQuantumDim`, which has no
instance. Item (1) is settled as a **growth class** — the period is
super-exponential by the $\surd$-branch argument of the colour cubic, confirmed
independently by the residue-sum route, and the object is identified as the
*q*-deformed involution number $T_q(n) = n\,\mathrm{lw}(n-1) \to I(n)$; what
remains open there is the exact *q*-statistic, for which no *q*-holonomic
recurrence exists at low depth. Note in particular that the falling factorial
$(1/2)_n$ is **not** a closed form for $\mathrm{lw}$ — it outgrows it, and no
constant geometric factor absorbs the difference. Item (3) is excluded rather than
open: $w_3$ is a required boundary condition of a rank-2 problem, a scope-(b)
result with its invariant cited (`no_scalar_kernel_on_carrier`).

The magnitude that matches experiment therefore depends on (1)–(3) as *inputs*, of
which (2) is the one still to be derived. See
[`2026-08-29-jet-filtration-three-inputs-corpus-grep.md`](../../../docs/audits/2026-08-29-jet-filtration-three-inputs-corpus-grep.md).
