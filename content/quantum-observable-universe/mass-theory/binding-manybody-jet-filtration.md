**Conjecture (binding many-body series = jet-order filtration).**

The per-isotope binding energy of the canonical braid $\mathcal{B}_K$ is the
**body-order series**

$$
B(K) \;=\; \sum_{n \geq 2} B_n(K),
\qquad
B_n(K) \;=\; m_e\,a_D^{(n)}(K)
\;=\; m_e\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}
\;=\; m_e\,2\pi i\!\!\sum_{p\,\in\,\mathcal{S}_c^{\mathrm{hyp}}}\!\!
        \operatorname{Res}_p\,\lambda_{\mathrm{SW}}^{(n)},
$$

in which the **body order $n$ is the vertical (jet) degree** of the prolonged
Seiberg--Witten differential
([`prop:mi-sw-abelianisation`](#prop:mi-sw-abelianisation)), the $n$-body term is
$m_e$ times the $n$-th prolonged SW period, and that period is the algebraic
residue sum of [`prop:sw-period-residue-sum`](#prop:sw-period-residue-sum) taken
over the **hyperbolic** components only (non-hyperbolic components contribute
$\operatorname{Vol}=0$). Equivalently: the many-body binding series **coincides
with the jet-order filtration** of $\mathcal{B}_K$, term by term.

The growth of the residue weights with body order — the empirical "$\rho\cdot A$"
scale rule — is conjectured to be the solution of a $q$-difference equation on
the binding generating function $G(x;q)=\sum_n B_n x^n$, namely
$G(qx;q)=R(q,x)\,G(x;q)$, whose Archimedean ($\tau$) image is a Dirac-type
partial differential equation. Under this conjecture $\rho\cdot A$ is an
**output** of the recursion, not a fitted constant.

**Anchors.** The series is pinned at two body orders already derived without
fitting: the $n=2$ deuteron term (single inter-nucleon bond) and the $n=4$
magic-shell term [`magic-A-binding-formula`](#prop:magic-A-binding-formula),
$B(^{4}\mathrm{He}) = 2\,m_e\,A\,\operatorname{Vol}(\mathrm{L6a4})$, which lands
$^{4}\mathrm{He}$ within $+5.87\%$. The conjecture asserts that these are the
$n=2$ and $n=4$ members of one filtration, with the $n=3$ term the genuine
three-body contribution (not reducible to pairwise sums).

This is an open conjecture: the residue-sum form of each term and the two
anchors are established, but the equality of the full binding to the complete
jet-order filtration — and the $q$-difference origin of the scale rule — are
not yet proved.

**Scope note on the weight $w_n(K)$ (2026-07-11).** A derive-or-refute of the
weight kernel (coordinated with PR #3534) establishes what does *not* close.
Body-order weights $w_n$ (shared across knots $K$) are **admissible**: the raw
$^{3}\mathrm{H}$/$^{3}\mathrm{He}$ binding split ($0.76\ \text{MeV}$, $9.9\%$) is
almost entirely **Coulomb** — on the Coulomb-corrected strong binding
$B_{\mathrm{strong}}$ the mirror pair agrees to $\sim 2.7\%$ (charge-symmetry
breaking), so a $K$-independent $w_n$ is *not* excluded. But no parameter-free
*constant-ratio* kernel $R(q,n)$ reproduces the extracted $w_2,w_3,w_4$ to $5\%$
(geometric $22.7\%$, $[n]_q$ $29.4\%$, $[n]_q^2$ $6.9\%$ the lone near-miss), and
a tuned recursion is the banned seventh $\Delta_\lambda$ ansatz. A fully
$K$-dependent kernel is underdetermined by the anchors ($A-1$ unknowns against
one equation per isotope) — extraction is a fit. Closure therefore requires the
*derived* $R(q,x)$. The eigenfunction relation of the na-Stokes period
$a_D^{(n)}=S(n)/n$ (the seed $c_3=[2]_q$ exact, and the Habiro
$(q-1)^2\Phi_3$ deviation, formalized in
[`QOU.Mass.BindingEigenfunctionTwoTier`](lean/QOU/Mass/BindingEigenfunctionTwoTier.lean))
supplies a *derived target* for $R(q,x)$ but does not determine it — the binding
deviation and the $Q_\beta$ $c_k$ ladder share the Habiro *ring*, not the same
element. See [`docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md`](../../../docs/audits/2026-07-11-eigenfunction-weight-kernel-link-and-wn-derive-or-refute.md).
