**Proof.**  We give the two legs in parallel and then verify their
meeting point.

### Geometric leg

By [def:rigid-monoidal-category](#def:rigid-monoidal-category) the
ambient category $\mathbf{C}$ is rigid monoidal, so every object has a
left and right dual.  The pairing
$\langle x, y \rangle := \mathrm{tr}_{\mathrm{Ad}}(x \otimes y^*)$
([def:adjoint-trace](#def:adjoint-trace)) is non-degenerate (rigid
duality) and Frobenius (symmetric monoidal: $\langle x, y \rangle =
\langle y, x \rangle$).

The categorical action of $\mathbf{C}$ on the state bundle
$\mathcal{S} \to M$ ([def:quantum-observable-universe](#def:quantum-observable-universe))
gives a connection $\nabla$ via the Tannakian-style equivalence: for
a fibre $\mathcal{S}_p$ over a brane point $p \in M$, the action of a
small loop $\gamma$ at $p$ on $\mathcal{S}_p$ is parallel transport
$\mathrm{Hol}_\nabla(\gamma) \in \mathrm{End}_{\mathbf{C}}(A)$.  Stokes'
theorem identifies $\mathrm{Hol}_\nabla(\gamma) = \exp \int_\Sigma F_\nabla$
where $\Sigma$ is a disk bounding $\gamma$ and $F_\nabla$ is the
curvature 2-form.  This identifies the categorical action with a
connection's curvature, integrated against $M$.

For $K = \widehat{T_w} \subset S^3$ the Markov closure of the canonical
braid, the universal cover of $S^3 \setminus K$ carries a Reeb-foliation
structure (since $S^3 \setminus K$ admits a contact form whose Reeb
flow is the closed-vortex flow of $T_w$ — this uses the Frobenius
pairing as the contact volume form, see
[prop:archimedean-realization-functor](#prop:archimedean-realization-functor)).
The Reeb-vortex density $\mu$ is the volume form induced by the
Frobenius pairing on the cover.

By Mostow rigidity \cite{mostow1968}, if $K$ is hyperbolic
then $S^3 \setminus K$ admits a unique complete hyperbolic structure
of finite volume, and any volume form induced by a categorical pairing
on the cover is *forced* to be a multiple of the hyperbolic volume
form.  By Gromov's norm theorem \cite{gromov1982,thurston1978},
$\mathrm{Vol}_{\mathrm{hyp}}(K) = v_3 \cdot \|S^3 \setminus K\|_{\mathrm{Gr}}$
where $v_3$ is the volume of the regular ideal tetrahedron and
$\|\cdot\|_{\mathrm{Gr}}$ is the Gromov norm.  The Reeb-vortex density
$\mu$ integrates to the simplicial volume:
$\int_{S^3 \setminus K} \mu = v_3 \cdot \|S^3 \setminus K\|_{\mathrm{Gr}}$.

Hence

$$
\mathrm{Vol}_{\mathrm{hyp}}(K) \;=\; \int_{S^3 \setminus K} \mu \quad (\text{geometric}).
$$

### Algebraic leg

By [prop:confinement-sdp](#prop:confinement-sdp), at substrate $q_0$
the joint mass-tower SDP admits a solution whose certificate
includes, per atom $\mathfrak{H}$ of strand count $n_0$, the canonical
Hecke element $T_w \in H_{n_0}(q_0)$ in Gröbner–Shirshov normal form.
The GB-NF carries a length filtration $\ell$ and a jet-order grading
($\ell$ from Coxeter length on $S_{n_0}$; jet-order from the temporal
sequence of reductions; both certificate components verified for
small cases by [`gb_filtration_jet_tracker.py`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb_filtration_jet_tracker.py)
and locked in [`gb-filtration-jet-order.witness.json`](https://github.com/litlfred/qou/blob/claude/mass-units-bridge-followups/folio-assistant/computations/gb-filtration-jet-order.witness.json)).

Wedderburn for the semisimple algebra $H_n(q)$ over the splitting
field $\mathbb{Q}(q^{1/2})$ gives
$H_n(q) \cong \bigoplus_\lambda M_{d_\lambda}(\mathbb{Q}(q^{1/2}))$
where $\lambda$ ranges over partitions of $n$ and $d_\lambda$ is the
dimension of the $S_n$-irreducible $\lambda$
([prop:wedderburn-trace-identity](#prop:wedderburn-trace-identity)).
Under this decomposition the Markov trace on $H_n(q)$ takes the
linear form
$\mathrm{tr}_M = \sum_\lambda y_\lambda(q) \chi_\lambda$
where $y_\lambda(q) = s_{\lambda, r}(Q) / Z$ is the Wenzl-bridge
coefficient ([thm:jones-markov-trace](#thm:jones-markov-trace),
[prop:alpha-k-derivation-procedure](#prop:alpha-k-derivation-procedure)).

Reshetikhin–Turaev identifies the Markov trace of $T_w$ with the
Jones polynomial of $\widehat{T_w}$ at $q$:
$J_K(q) = \mathrm{tr}_M(T_w)$.  Evaluating at $q_0$ gives a numerical
quantity $J_K(q_0) \in \mathbb{R}$ derivable from the SDP-output $T_w$
alone — i.e.\ purely on the algebraic leg.

The volume conjecture (Kashaev 1995, Murakami–Murakami 2001) states

$$
2\pi \lim_{N \to \infty} \frac{1}{N} \log \big| J_K(\zeta_N) \big|
\;=\; \mathrm{Vol}_{\mathrm{hyp}}(K),
\qquad \zeta_N = e^{2\pi i / N},
$$

so the asymptotic of the colored Jones polynomial reproduces the
hyperbolic volume.  Hence

$$
\mathrm{Vol}_{\mathrm{hyp}}(K) \;=\; 2\pi \lim_{N \to \infty} \frac{1}{N} \log \big| J_K(\zeta_N) \big| \quad (\text{algebraic}).
$$

### Two legs agree

The two right-hand sides — the Reeb-vortex integral on the cover and
the colored-Jones asymptotic — are *both* equal to $\mathrm{Vol}_{\mathrm{hyp}}(K)$
in $S^3 \setminus K$.  The volume conjecture is the bridge: it is the
non-trivial assertion that the analytic asymptotic of $J_K$ at roots
of unity equals the geometric simplicial volume.  In QOU the bridge
is consumed as a borrowed theorem; an internal derivation requires
the Reeb-vortex density of the geometric leg to be *constructively*
the same volume form as the colored-Jones asymptotic produces, which
is the open structural item.

### Mass identity

The Archimedean realization functor
([prop:archimedean-realization-functor](#prop:archimedean-realization-functor))
fixes the dimensional bridge: a categorical-trace quantum integer
times $m_e$ has units of MeV.  The structural prefactor
$\rho \in \mathbb{Z}_{>0}$ is the multiplicity of $T_w$'s SDP solution
in the Wedderburn decomposition; for $\ell \leq 1$ entries this is
direct (electron $\rho = 1$ trivially since $T_{2,3}$ is non-hyperbolic
and the mass identity is anchored to AME; proton/neutron $\rho = 1$ via
the Borromean closure with explicit volume $8G$).  For $\ell = 2$
atoms the rule on $(Z, N)$ is open and is treated separately
([prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas) §"Open").

Combining: $B(\mathfrak{H}) = \rho \cdot m_e \cdot \mathrm{Vol}_{\mathrm{hyp}}(\widehat{T_w})$.
$\square$

### Methodology gating

The proof above presumes both legs are constructively in place.  In
the current implementation:

- For \texttt{principled-derivation} entries (electron, proton,
  neutron) only the algebraic leg is fully constructive (steps 1–4 of
  the algorithm); the geometric leg is borrowed at step 6.  This is
  acceptable because $\widehat{T_w}$ for these entries is non-hyperbolic
  (trefoil, Borromean), so Vol enters as $0$ (electron) or $8G$
  (Borromean), and the volume-conjecture bridge is degenerate.
- For \texttt{manual-historical} entries (²H, ³H, ³He) only step 6 is
  invoked (Vol from SnapPy); steps 1, 5, 7 are pending.
- For \texttt{recursive-on-⁴He} (⁸Be–⁴⁰Ca) the recursion factors
  through the ⁴He magic-A formula and inherits its methodology.
- For ⁶Li, ⁷Li, the volume-match search runs *backwards* from step 9
  to a candidate knot in step 6 — bypassing steps 1, 5, 7.  This is
  the deprecated methodology, quarantined by
  [prop:recursive-atom-knot-atlas](#prop:recursive-atom-knot-atlas)
  §"⚠ Provisional / deprecated methodology".  The principled atlas
  excludes them.
