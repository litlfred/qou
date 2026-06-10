# Koide's $Q = 2/3$ in QOU: the reduction, the gap, and the derivation path

**Date:** 2026-06-10
**Branch:** `claude/lucid-brown-4vfod4`
**Status:** analysis + roadmap. The elementary reduction (§1) is rigorous and
standard in the Koide literature; the QOU-specific *forcing* of the balance
condition (§2–§4) is **open**, and the only non-circular path to closing it is
specified here.

## 0. Summary

Koide's empirical relation for the charged leptons,
$$
Q = \frac{m_e+m_\mu+m_\tau}{\bigl(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau}\bigr)^2}
  = \frac{2}{3}
  \qquad(\text{experiment: } 0.666661(7)),
$$
has **no accepted first-principles derivation**: Koide (1981) *noticed* it inside
a preon model whose assumptions did not survive, and the physics community files
it as an intriguing empirical relation. This document

1. reduces "QOU derives Koide" to a **single structural condition** on the lepton
   $\sqrt{\text{mass}}$ vector,
2. records exactly what QOU currently supplies and **where the gap is**, and
3. specifies the **only non-circular path** to closing it.

## 1. The reduction (rigorous; standard in the Koide literature)

**Setup.** Write $x_i = \sqrt{m_i} > 0$ for $i \in \{e,\mu,\tau\}$ and
$Q = \bigl(\sum_i x_i^2\bigr)/\bigl(\sum_i x_i\bigr)^2$. Decompose
$\vec x = (x_e,x_\mu,x_\tau) \in \mathbb{R}^3$ along the **democratic axis**
$\hat d = (1,1,1)/\sqrt3$:
$$
\vec x = a\,\hat d + \vec s,
\qquad a = \vec x\cdot\hat d = \tfrac{1}{\sqrt3}\textstyle\sum_i x_i,
\qquad \vec s \perp \hat d .
$$
Here $a\hat d$ is the projection onto the **trivial** representation of the
generation symmetry ($S_3$, or its cyclic subgroup), and $\vec s$ is the
**standard-representation** (traceless) part.

**Proposition (reduction).**
$$
Q = \frac{1}{3} + \frac{|\vec s|^2}{3a^2},
\qquad\text{hence}\qquad
Q \in \Bigl[\tfrac13,\,1\Bigr)
\quad\text{and}\quad
\boxed{\,Q = \tfrac23 \iff |\vec s| = a\,}.
$$

*Proof.* $\bigl(\sum_i x_i\bigr)^2 = (\sqrt3\,a)^2 = 3a^2$, and by orthogonality
$\sum_i x_i^2 = |\vec x|^2 = a^2 + |\vec s|^2$. Dividing,
$Q = (a^2+|\vec s|^2)/(3a^2) = \tfrac13 + |\vec s|^2/(3a^2)$. Since $a > 0$:
$Q \ge \tfrac13$ with equality iff $\vec s = 0$ (all masses equal); and
$3a^2 - |\vec x|^2 = 2\sum_{i<j}x_ix_j > 0$ gives $Q < 1$. Setting $Q = \tfrac23$
forces $|\vec s|^2 = a^2$. $\qquad\blacksquare$

**Four equivalent forms of the balance condition $|\vec s| = a$.**

1. **Length balance** — the trivial-rep part and the standard-rep part of
   $\vec x$ have equal norm.
2. **$45^\circ$ condition** — $\cos\angle(\vec x,\hat d) = a/|\vec x| = 1/\sqrt2$,
   i.e. $\vec x$ sits at $45^\circ$ to the democratic axis.
3. **Circulant $\sqrt2$ form** — $x_k = \mu_0\bigl(1 + \sqrt2\cos(\delta + \tfrac{2\pi k}{3})\bigr)$,
   $k=0,1,2$ (check: $\sum_k x_k = 3\mu_0$, $\sum_k x_k^2 = 6\mu_0^2$, so $Q = 6/9$).
4. **Polynomial form** — $\sum_i x_i^2 = 4\sum_{i<j} x_i x_j$, equivalently
   $3\sum_i m_i = 2\bigl(\sum_i \sqrt{m_i}\bigr)^2$.

This reduction is elementary and standard (Foot's $45^\circ$; the
democratic/circulant parametrisation). It is reproduced here only to fix the
**exact target**:

> QOU derives Koide **iff** QOU forces $|\vec s| = a$ on the lepton
> $\sqrt{\text{mass}}$ vector — from machinery fixed *before* looking at the
> value $2/3$.

The entire physical content of Koide is the one equation $|\vec s| = a$.
Everything downstream (the value $2/3$, the $m_\tau$ prediction) is then trivial.

## 2. What QOU currently supplies — and the gap

Findings from the lepton sector (`content/quantum-observable-universe/`):

| Item | State | Source |
|------|-------|--------|
| Lepton-mass tower $\mathfrak m(K_\ell) = m_e\,\mathcal F_\ell(q)$ | **Conjecture**, not theorem | `mass-theory/lepton-mass-tower-canonical.md` (opens *"Conjecture (canonical lepton-mass tower)"*) |
| $\tau$ braid representative | **Unpinned** — "tau analogously" | same file (gives $K_{\mathfrak e}=\sigma_1^3$, $K_\mu=(\sigma_1\sigma_2^{-1})^2$, then "tau analogously") |
| $m_\tau/m_e = 3477.23$ | quoted as **CODATA target** | same file — **circularity flag** |

**Circularity flag.** If $K_\tau$ is chosen so that $\mathcal F_\tau(q)$
reproduces $m_\tau/m_e = 3477$, then "deriving Koide" is circular: the *measured*
lepton masses already satisfy Koide, so fitting $\tau$ to the measured mass proves
nothing. The derivation must pin $\tau$ **independently of its mass**.

So: the reduction (§1) is proved; the **forcing of $|\vec s| = a$ is not**,
because the object that would force it (the $\tau$ assignment + a *proved* mass
law) is still open.

## 3. The lepton braid tower

$$
\text{electron } K_{\mathfrak e} = \sigma_1^3 \in H_2(q)\ (\text{trefoil}),
\qquad
\text{muon } K_\mu = (\sigma_1\sigma_2^{-1})^2 \in H_3(q)\ (\text{figure-eight } 4_1),
\qquad
\text{tau } K_\tau = ?\ \in H_4(q).
$$

The lepton mass law is the **conjectural per-braid Markov-trace functional**
$\mathcal F_\ell(q)$ — *not* the (for leptons, superseded) volume–density product
$\mathrm{Vol}(K)\cdot\rho/\hbar_q^2$. Pinning the tower rule that sends
$\sigma_1^3 \mapsto (\sigma_1\sigma_2^{-1})^2 \mapsto (\,\cdot\,)$ canonically into
$H_4$ is the first concrete sub-task.

## 4. The non-circular derivation path

1. **Pin $K_\tau \in H_4$ by the structural tower rule** — never by $m_\tau$.
2. **Compute $\mathcal F_\tau(q)$** (Markov trace) → an *independent* $m_\tau$.
3. **Check $|\vec s| = a$** on the three predicted $\sqrt{\text{mass}}$ values.
   - Falls out ⇒ **Koide is a QOU theorem**, and $m_\tau \approx 1777$ MeV is a
     parameter-free prediction.
   - Does not ⇒ **QOU does not predict Koide** — itself a clean, publishable
     finding.

**Win condition (the version worth a senior sniff-test).** Prove $|\vec s| = a$
as an **exact structural identity** about $(\mathcal F_e, \mathcal F_\mu,
\mathcal F_\tau)$, independent of the numerical mass values. That is "Koide proved
in QOU," and it simultaneously predicts $m_\tau$ from $m_e, m_\mu$.

**Caveat.** QOU's *own* predicted $m_\mu$ is currently $9.6\sigma$ from CODATA
(the $\mu$–$p$ tension; `per-observable-100x-status.witness.json`). So the three
QOU $\sqrt{\text{mass}}$ values will not satisfy Koide *exactly* unless that
tension also resolves. The balance must emerge from the fixed braid rule, not be
rescued by the anchor choice.

## 5. Connection to the H3 Wedderburn machinery (landed on `main`, 2026-06-10)

The balance condition $|\vec s| = a$ is a statement about the **trivial-rep vs
standard-rep weights** of the $\sqrt{\text{mass}}$ vector. The Wedderburn
projector / idempotent work just landed on `main` (H3 Wedderburn projectors,
Poincaré-polynomial normalizers) is precisely the trivial⊕standard decomposition
tooling, and is the natural instrument for expressing $a$ and $|\vec s|$ inside
$H_3$/$H_4$. The $\tau$-forcing computation (§4) should be built on top of it.

## 6. The $\xi_m$ tower finding (background probe, 2026-06-10) and the joint-vs-individual pivot

A conjectural lepton closure factor *does* exist
(`mass-theory/conj-lepton-tower-h-n-plus-1-branching.md`):
$$
\xi_m = \frac{[2m-1]_q\,[m]_q}{[2m]_q}\cdot\frac{1}{\hbar_q^2},
\qquad
\mathcal F_\ell(q)\ \stackrel{\text{conj}}{=}\ \xi_\ell(q)\cdot\mathrm{Vol}_q^{\text{tower}}(K_\ell),
$$
with the triple $(2m-1,\,m,\,2m)$ reading as (bar-anti-symmetric, middle,
bar-symmetric) at lepton level $m$. **Muon ($m=2$) is the first member of the
pattern; tau ($m=3$, $\xi_3=[5]_q[3]_q/[6]_q$) already misses by $0.79\%$** — the
per-lepton closed form is not yet right at tau, and the form of $\xi_\ell$ is open
(Path A derivation / Path B fit / Path C Kashaev postulate — all open).

**Strategic consequence — prove the joint Koide relation, not the per-lepton
masses.** Koide ($|\vec s| = a$) is a *single* equation on the three masses; the
$\xi\times\mathrm{Vol}$ tower is *three* equations (one exact mass each) and
already fails the third at $0.79\%$ — about $10^3\times$ worse than Koide's
experimental $10^{-5}$. Therefore:

- Koide is the **better-supported, cleaner invariant** (1 equation, $10^{-5}$)
  than the per-lepton tower (3 equations, tau $0.79\%$ off).
- A proof of $|\vec s| = a$ would **predict $m_\tau$** from $m_e, m_\mu$ — turning
  the tower's failing tau into an *output* and making the $0.79\%$ per-lepton miss
  irrelevant.
- **Recommended attack:** derive $|\vec s| = a$ as a structural identity using the
  Wedderburn trivial/standard projectors (§5) **directly**, without first nailing
  each $\mathcal F_\ell$. The joint relation may hold even where the individual
  closed forms do not.

**Caveat (formalize-first).** The q-integer structure is suggestive — e.g.
$[2]_q=\sqrt2$ at a primitive 8th root of unity, and $[3]$-type factors carry
3-fold structure — but the balance must be shown at the *real* substrate
$q_0\approx1.1097$ (or as a $q$-independent identity), **not** by hunting a
root-of-unity where $\sqrt2$ happens to appear. That hunt is the numerology trap.

## 7. Lean formalisation

The reduction (§1) is elementary real algebra over $\mathbb{R}$:

- the iff $Q = \tfrac23 \iff 3\sum m_i = 2(\sum\sqrt{m_i})^2$ is `field_simp` +
  `ring` / `nlinarith`;
- the range $Q \in [\tfrac13, 1)$ is `positivity` / `nlinarith`.

No `sorry` is needed for the reduction itself. It should be added as a
`proposition` content block in `mass-theory/` once (a) the Lean env is available
(currently: `elan`/`lake exe cache get` 403 in this sandbox) and (b) the
$\tau$-side is pinned, so the block can state the QOU-conditional form. Until then
this document is the human-checkable record of the proof.
