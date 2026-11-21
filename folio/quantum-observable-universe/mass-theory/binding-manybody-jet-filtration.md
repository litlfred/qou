**Conjecture (binding many-body series = jet-order filtration).**

The per-isotope binding energy of the canonical braid $\mathcal{B}_K$ is the
**body-order series**

$$
B(K) \;=\; \sum_{n \geq 2} B_n(K),
\qquad
B_n(K) \;=\; m_e\,a_D^{(n)}(K)
\;=\; m_e\oint_{\mathcal{S}_c}\lambda_{\mathrm{SW}}^{(n)}
\;=\; m_e\,2\pi i\!\!\sum_{p\,\in\,\mathcal{S}_c^{\mathrm{hyp}}}\!\!
        \mathrm{Res}_p\,\lambda_{\mathrm{SW}}^{(n)},
$$

in which the **body order $n$ is the vertical (jet) degree** of the prolonged
Seiberg--Witten differential
([Abelianisation of the MI integral on exceptional divisors](#prop:mi-sw-abelianisation)), the $n$-body term is
$m_e$ times the $n$-th prolonged SW period, and that period is the algebraic
residue sum of [The Seiberg–Witten period is an algebraic residue sum](#prop:sw-period-residue-sum) taken
over the **hyperbolic** components only (non-hyperbolic components contribute
$\mathrm{Vol}=0$). Equivalently: the many-body binding series **coincides
with the jet-order filtration** of $\mathcal{B}_K$, term by term.

The growth of the residue weights with body order — the empirical "$\rho\cdot A$"
scale rule — is conjectured to be the solution of a $q$-difference equation on
the binding generating function $G(x;q)=\sum_n B_n x^n$, namely
$G(qx;q)=R(q,x)\,G(x;q)$, whose Archimedean ($\tau$) image is a Dirac-type
partial differential equation. Under this conjecture $\rho\cdot A$ is an
**output** of the recursion, not a fitted constant.

**Anchors.** The series is referred to two body orders: the $n=2$ deuteron term
(single inter-nucleon bond) and the $n=4$ magic-shell term
[`magic-A-binding-formula`](#prop:magic-A-binding-formula),
$B(^{4}\mathrm{He}) = \rho_F\,m_e\,A\,\mathrm{Vol}(\mathrm{L6a4})$ with
$\rho_F = 2$, which lands $^{4}\mathrm{He}$ within $+5.87\%$. The conjecture
asserts that these are the $n=2$ and $n=4$ members of one filtration, with the
$n=3$ term the genuine three-body contribution (not reducible to pairwise sums).

**What the two anchors do and do not pin.** Read with the weight $w_n$ of the
scope note below, the unknowns through $A=4$ are $w_2,w_3,w_4$ — three — against
two anchor equations, so **one free parameter survives and the $n=3$ term is not
determined**. The $n=2$ anchor fixes $w_2$; the $n=4$ anchor is a single equation
in the two remaining unknowns, so for every $w_3$ there is exactly one
$w_4 = (B_{\mathrm{magic}}/m_e - a_D^{(2)}w_2 - a_D^{(3)}w_3)/a_D^{(4)}$ holding
both anchors identically. The $A=3$ prediction along that family,
$B(^{3}\mathrm{H}) = m_e(a_D^{(2)}w_2 + a_D^{(3)}w_3)$, is unbounded in $w_3$, so
$A=3$ cannot test the $n=3$ term — it defines it. Adding positivity and monotone
growth $w_2 \leq w_3 \leq w_4$ narrows the induced $B(^{3}\mathrm{H})$ to a window
$66$–$78\%$ of the observable's own magnitude, which the data does satisfy; that
consistency is the one non-circular check the anchors support, and it carries
that width. The count is unchanged if the $n=4$ anchor is instead read as pinning
the $n=4$ term alone, since nothing then mentions $w_3$ at all.

Neither anchor is parameter-free as stated. The prefactor $\rho_F = 2$ is
**consumed as an input hypothesis**, not derived — see
[the doubly-magic binding context](#rem:magic-A-binding-formula-context). And the
$w_2 = 4.353$ used across the $w_n$ probes is $B_{\mathrm{AME}}(^{2}\mathrm{H})$
inverted, an extraction; the *derived* single $p$–$n$ bond gives
$\alpha L_{pn} \approx 2.833\ \mathrm{MeV}$, $+27.3\%$ above the measured
$2.2246\ \mathrm{MeV}$, hence $w_2 \approx 5.544$ instead. Rigidity for $w_3$
would have to come from the *derived* kernel $R(q,x)$, which is open. Measured in
[the $n=3$ forcing probe](../../../computations/binding_n3_forcing_probe.py);
scope-(a) analysis in
[the n=3 forcing audit](../../../docs/audits/2026-08-26-n3-body-order-forcing.md).

This is an open conjecture: the residue-sum form of each term is established
and the two anchors are stated, but the anchors are conditional in the sense
just described, they leave the $n=3$ term free, and the equality of the full
binding to the complete jet-order filtration — together with the $q$-difference
origin of the scale rule — is not proved.

**Scope note on the weight $w_n(K)$.** A derive-or-refute probe of the
weight kernel establishes what does *not* close.
Body-order weights $w_n$ (shared across knots $K$) are **admissible**: the raw
$^{3}\mathrm{H}$/$^{3}\mathrm{He}$ binding split ($0.76\ \text{MeV}$, $9.9\%$) is
almost entirely **Coulomb** — on the Coulomb-corrected strong binding
$B_{\mathrm{strong}}$ the mirror pair agrees to $\sim 2.7\%$ (charge-symmetry
breaking), so a $K$-independent $w_n$ is *not* excluded. That $2.7\%$ is
geometry-dependent: at the canonical *derived* $r_0 = \hbar c/m_\pi$ of
the Coulomb-energy computation the correction overshoots and the residual is $\approx -1\%$
with $^{3}\mathrm{He}$ the more bound partner, while the measured-charge-radius
geometry gives $+1\%$; the spread across geometries is $0.16\ \mathrm{MeV}$,
which does not affect the admissibility conclusion. But no parameter-free
*constant-ratio* kernel $R(q,n)$ reproduces the extracted $w_2,w_3,w_4$ to $5\%$
(geometric $22.7\%$, $[n]_q$ $29.4\%$, $[n]_q^2$ $6.9\%$ the lone near-miss), and
a tuned recursion is the banned seventh $\Delta_\lambda$ ansatz. A fully
$K$-dependent kernel is underdetermined by the anchors ($A-1$ unknowns against
one equation per isotope) — extraction is a fit. Closure therefore requires the
*derived* $R(q,x)$. The eigenfunction relation of the na-Stokes period
$a_D^{(n)}=S(n)/n$ (the seed $c_3=[2]_q$ exact, and the Habiro
$(q-1)^2\Phi_3$ deviation, both proved)
supplies a *derived target* for $R(q,x)$ but does not determine it — the binding
deviation and the $Q_\beta$ $c_k$ ladder share the Habiro *ring*, not the same
element.

**How much is undetermined, exactly, and why no scalar $R(q,x)$ can supply it.**
"Does not determine it" is now a count rather than a caution. With $R$ an
unconstrained formal power series the shift relation determines exactly one
kernel coefficient per body order, and conversely: for any body sequence with
$B_2 \neq 0$ the map $\{r_k\} \leftrightarrow \{B_n\}$ is a **bijection**
(proved).
So the unconstrained ansatz constrains *nothing*: it reparametrises
the unknown weights, it does not remove them, and "$\rho\cdot A$ is an output of
the recursion" is false unless $R$ is independently pinned. All of the ansatz's
content therefore lies in the **finiteness** of the Laurent window.

A multi-anchor test (D$\to{}^{12}$C, Coulomb-corrected) further shows that the
full-tower reading — summing $B(K)=\sum_{n=2}^{A} m_e\,a_D^{(n)}\,w_n$ to the
nucleon count $A$ — is **refuted for $A\geq 5$**: the na-Stokes period $a_D^{(n)}$
grows super-exponentially while $B/A\to\mathrm{const}$, so any bounded or
amplifying body-order weight overshoots ($\sim{+}920\%$ at ${}^{6}$Li,
$\sim{+}2\times10^{6}\%$ at ${}^{12}$C). The series must therefore be a **few-body
truncation** (fixed small $n_{\max}$, a $2$–$3$-body cluster count $\times$
A-multiplicity, matching nuclear $2$-/$3$-body force dominance), not a sum to $A$;
the na-Stokes period remains the correct *light*-nucleus ($A\leq 4$) kernel.
