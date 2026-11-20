**Conjecture (complex-volume unification of mass-binding and decay).** [Lean classes: `ComplexVolumeMatch` / `SingleFrakVAssembly` / `StageCSigma3Lift`]
*Binding and the $\beta$-decay $Q$-value form
the real and imaginary parts of a single complex fibre observable — the
complexified mass-endomorphism convolution-defect*

$$
  \mathfrak{V}(K)\;=\;E_0\,\mathrm{tr}_M\big((\Pi_{\text{free}} - \mathbf{1})\circ\mathcal{M}\big)
  \;\in\;\mathbb{C},
  \qquad
  \mathfrak{E}_{\mathrm{bind}}(K) = \mathrm{Re}\mathfrak{V}(K),
  \quad
  \mathfrak{Q}_\beta(K) = \mathrm{Im}\mathfrak{V}(K),
$$

*the QOU analogue of the Neumann–Zagier complex volume
$\mathbb{V}(K) = \mathrm{Vol}(K) + i\,\mathrm{CS}(K)$ \cite{neumann-zagier1985},
computed simplicially as a sum of Rogers dilogarithms of the tetrahedron
parameters \cite[Thm.~1]{neumann-cspaper}.*

## The one object

Categorically — **no braid words**. For a confined knot $K$:

- $\mathcal{M} = \mathcal{M}(K) \in \mathrm{End}_{\mathbf{C}}(X_K)$
  forms the mass endomorphism of the object $X_K$ representing $K$ in
  the rigid monoidal category $\mathbf{C}$.
- $\mathrm{tr}_M : \mathrm{End}_{\mathbf{C}}(X_K) \to k$ provides the
  categorical Markov trace (the closed/categorical trace; the fibre functor $\tau$ is a *different* object, never
  $\mathrm{tr}_M$).
- $\Pi_{\text{free}} \in \mathrm{End}_{\mathbf{C}}(X_K)$ provides the
  idempotent projector ($\Pi_{\text{free}}^2 = \Pi_{\text{free}}$)
  onto the factorized sub-object
  $X_K \twoheadrightarrow X_1 \otimes \cdots \otimes X_c$ — the
  constituents un-linked (the categorical projection onto the split
  tensor: the same R-matrix braiding with the inter-constituent
  confining crossings dropped).

The convolution-defect measures the categorical trace of the part of
$\mathcal{M}$ that does *not* survive $\Pi_{\text{free}}$ — a
projection defect (no words, no overloaded $\Delta$, no new
trace-like symbol):

$$
  \mathrm{tr}_M\big((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M}\big)
  \;=\;
  \mathrm{tr}_M(\Pi_{\text{free}}\circ\mathcal{M}) - \mathrm{tr}_M(\mathcal{M})
  \;=\;
  \sum_\lambda y_\lambda\,\big(\chi^\lambda(\Pi_{\text{free}}\mathcal{M}) - \chi^\lambda(\mathcal{M})\big),
$$

the per-partition object of the canonical binding
([Categorical mass as Markov trace](#prop:categorical-mass-markov),
`binding_canonical`). This describes **any confined knot $K$**.
The nuclear binding case — a nucleus is a confined nucleon knot,
factorized sub-object $\mathfrak{p}^{Z}\otimes\mathfrak{n}^{N}$ — forms the
physical instance $\mathrm{tr}_M(\mathcal{M}) = \mathrm{tr}_M(W_{\text{atom}})$
of `binding_canonical`. Read over $\mathbb{C}$ the defect carries **one
bit more information than either observable alone**: its two
bar-parities.

## Forcing of Re/Im — the bar-parity = the complexification

Write $q = e^{\lambda}$, $\lambda = \log q$. The two crossing
eigenvalues $q, -q^{-1}$ split as

$$
  \underbrace{\tfrac{q+q^{-1}}{2}=\cosh\lambda}_{\textbf{bar-even}},
  \qquad
  \underbrace{\tfrac{q-q^{-1}}{2}=\sinh\lambda}_{\textbf{bar-odd}},
$$

so $\cosh\lambda \pm \sinh\lambda = e^{\pm\lambda}$. The bar-even and
bar-odd parts constitute **one element $e^{\lambda}$ read on its two
parities**. Continue $\lambda \mapsto i\theta$ (the substrate $q$ rotated
onto the unit circle / a root of unity) and $\cosh\to\cos$,
$\sinh\to i\sin$: the **bar-even/bar-odd split becomes a Re/Im split**.
That exactly constructs the complex volume:

| | real part (bar-even, $\cosh$, real $q$) | imaginary part (bar-odd, $\sinh$, root-of-unity $q$) |
|---|---|---|
| **Neumann–Zagier** | $\mathrm{Vol}(K)$ (hyperbolic) | $\mathrm{CS}(K)$ (Chern–Simons) |
| **QOU** | $\mathfrak{E}_{\mathrm{bind}}(K)$ — **binding / mass** | $\mathfrak{Q}_\beta(K)$ — **$\beta$-decay** |

The mass/binding channel provides the **volume** (real, $\cosh$) part; the
decay channel provides the **Chern–Simons** (imaginary, $\sinh$) part of the
same $\mathfrak{V}$.

## Established results, and the fibre-level caveat

- **Proved (algebra).** The bar-parity decomposition
  $\tfrac{q+q^{-1}}{2}\pm\tfrac{q-q^{-1}}{2} = q^{\pm1}$ holds over any
  field. The complex reconstruction $\mathfrak{E}_{\mathrm{bind}}+i\,\mathfrak{Q}_\beta
  = \mathfrak{V}$ follows from the two projection
  hypotheses ([Lean](#conj:binding-qbeta-complex-volume),
  `QOU.MassEndomorphism.ComplexVolumeUnification`, 0 sorries).
- **Proved (classical limit).** The free/factorized projection
  $\chi^\lambda_{\text{free}}$ forms the disjoint-product factorization,
  proven at $q=1$ via Plancherel duality
  ([Block-multiplicativity of per-generator $\hat{V}$ on the disjoint Hecke product](../mass-theory/block-multiplicativity-v-free.md)).
  The $q$-deformed case remains class-axiomatized (conjectural).
- **Conjectural (the unification itself).** We conjecture that the physical binding
  and $\mathfrak{Q}_\beta$ construct the Re/Im of the **same** $\mathfrak{V}$
  at a single normalization.
- **Literature.** Geometric complex volumes carry a quantum tower: the quantum
  hyperbolic field theory partition functions $H_N$, whose $N = 1$ member
  coincides with the Cheeger–Chern–Simons invariant and which obey surgery
  formulas for cusped manifolds \cite[\S6, Thm.~6.4]{baseilhac-benedetti2007}.
  $\mathfrak{V}$ is only conjecturally such a volume.
- **Fibre-level caveat (STRICT).** At the **archimedean / observable**
  level $\mathrm{Im}(q_0)=0$
  (`lusztig_q_0_imaginary_part_zero`): binding and $\mathfrak{Q}_\beta$ both measure
  real numbers. The complex structure is therefore
  **fibre-level** (pre-$\tau$). $\mathfrak{V}(q)$ provides a complex object in
  the fibre, and $\mathfrak{E}_{\mathrm{bind}}$, $\mathfrak{Q}_\beta$ provide its Re/Im
  **shadows under different archimedean evaluations** (real-$q$ vs
  root-of-unity). There is no "complex mass" — there is one complex
  fibre object with two real observable shadows, exactly as
  $\mathrm{Vol}$ and $\mathrm{CS}$ are separately real.


## The open single-$\mathfrak{V}$ assembly and the $\zeta_4$-faithfulness constraint

The complex-volume model $V_0(z) = \cosh z + i\sinh z$ satisfies the **$\zeta_4$-partner relation**: $V_0(z + i\pi/2) = -\cosh z + i\sinh z$, exactly negating the bar-even (binding) channel while keeping the bar-odd ($Q_\beta$) channel. The full $\zeta_4$-orbit decomposes the model into exactly the two **faithful** eigencomponents (trivial and sign isotypes vanish).

**Constraint on the open assembly:** Any candidate physical assembly $\mathfrak{V}$ must be **$\zeta_4$-faithful** (supported entirely on the $\pm i$ characters of $\mathbb{Z}_4$). A candidate with a nonzero orbit sum or sign isotype is falsified (`QOU.Mass.ComplexVolumeZeta4Partner.SingleFrakVAssembly`). This structural consequence forces $\zeta_4^2 = -1$ on the assembly, providing non-degenerate conditional content for the conjecture class.


## The open Stage-C $\sigma_3$-lift obligation

The holomorphic tie hypothesis demands that a **single** Askey-Wilson three-term recurrence carries both the binding (bar-even) and $Q_\beta$ (bar-odd) ladders. This implies the Casoratian $W_k$ of the two ladders maintains a constant sign pattern forced by the recurrence parameters.

**Constraint on the lift:** The categorical $\sigma_3$-lift $\Lambda \in H_4(q)$ of the decay operator must supply genuine $c_4$ rungs that satisfy this sign constraint (`QOU.QBeta.StageC.StageCSigma3Lift`). Any valid lift that leads to a sign-incompatible Casoratian $W_3 \le 0$ (given $W_2 > 0$) refutes the one-recurrence identification, serving as a parameter-free kill-test on candidate objects.

## The S channel through $\Phi_b$ (conditional wiring)

For the bar-odd S observable ($S = c_3 + \mathrm{Vol}(4_1)$), the
conjecture's decay side takes the concrete form
$S(q_0) = \mathrm{Im}\,\mathfrak{V}\bigl(u(q_0)\bigr)$: the Chern–Simons
part of the **deformed** complex volume at the substrate deformation
$u(q_0)$ (log meridian holonomy). The deformed volume itself is a
theorem for $4_1$ and explicitly computable via Neumann–Zagier; the two
open inputs — the map $u(q_0)$ and the channel identity — are carried by
the class `QOU.QBeta.PhiBSArgumentIdentification.SDeformedVolumeChannel`.
Composed with the argument identification of
([algebraic-geometric dilogarithm equivalence](../mass-theory/algebraic-geometric-dilog-equivalence.md)),
three statements are derived unconditionally from the two classes
(`phase_eq_im_deformed_volume`, `phiB_eq_cs_phase`,
`exists_cs_vanishing`): the fibre-branch $\Phi_b$ phase at the
identified argument **is** the deformed Chern–Simons part; the $\Phi_b$
readout is the pure phase $e^{i\,\mathrm{CS}(u(q_0))}$; and *if* $S$ flips
sign between the anchors, that forces a substrate point $q^{*}$
where $\mathrm{Im}\,\mathfrak{V}(u(q^{*})) = 0$ — the deformed complex
volume purely real. This last is **conditional on a sign flip the data
does not establish**: each anchor value carries a CAL-3 propagated
uncertainty of $\pm 1.26$ ($130\times$ / $32\times$ the value); only the swing
$S(\text{muon}) - S(\text{proton})$ is resolved (the cross-anchor $c_3$
difference, with $\mathrm{Vol}(4_1)$ cancelled). So it is a conditional
structural statement, not an established prediction. This makes precise that $\Phi_b$ touches binding **only**
through this channel: remove the `SDeformedVolumeChannel` hypothesis and
no binding statement about $\Phi_b$ survives. On the open map $u(q_0)$
itself, the Neumann–Zagier leading-form family laws are proved
(`QOU.QBeta.UDeformFamilyPruning`) over the corrected harmonic form
$\mathrm{Im}\,\mathfrak{V}(u) = (\sqrt{3}/4)(\mathrm{Re}^2 u - \mathrm{Im}^2 u)$
(cusp modulus $\tau = -i\sqrt{3}$, so the leading coefficient
$a_2 = i\sqrt{3}/4$ is purely imaginary): all three candidate families —
fixed-phase ($\mathrm{Re},\mathrm{Im} \propto d$), phase-crossing
($\mathrm{Re} \propto d$, $\mathrm{Im} \propto d^{2}$), and
transverse-constant ($\mathrm{Re} \propto d$, $\mathrm{Im}$ anchor-constant),
with $d = q - q^{*}$ — are **refuted**: each is even in $d$, hence the same
sign on both sides of $q^{*}$, so none can produce a sign flip
$S(\text{muon}) > 0 > S(\text{proton})$ *were one present*. The surviving
necessary condition is that $u(q_0)$ must cross the diagonal
$|\mathrm{Re}\,u| = |\mathrm{Im}\,u|$ between the anchors; $u(q_0)$ itself
stays open. The measured values live in the probe witness, never in the
Lean, and the individual anchor signs are not resolved by the data; the resolved
target is the swing $S(\text{muon}) - S(\text{proton})$, and the onward
identification of this channel with the resurgent monodromy datum
$A_\omega$ is unsupported (no literature; integrality) and not carried.

## Computational corroboration

The two channels construct distinct real components of one object: the
$E_0\cdot|\Delta(\mathrm{net})|$ **net-route** (the bar-even, binding-like
$E_0\cdot\Delta(\mathrm{tr})$) provides a precision-ladder $c_2 \approx -8.0$,
whereas the canonical $c_2 = -1$ lives in the bar-odd $\mathrm{tr}_M$
**brane-tower** ladder
(witness `qbeta-ck-sseries-operator-match`). Two different real $c_2$'s for
the two parities align with Re/Im components of one complex
$c_2$.

## Corollary — one story, and one proof

Conditional on the unification, the framework's mass/binding chapter and
its $\beta$-decay chapter form **one derivation**: compute the complex
defect $\mathfrak{V}(K)$ once. Its real part yields every binding energy. Its
imaginary part yields every $Q$-value. The $\mathfrak{Q}_\beta$ residual
($-43.16\%$ at the ruled convention-D base; $+0.17\%$ under the retired Form A) and the binding $\Delta_\lambda$ gap become the *same* unclosed
object — the imaginary and real parts of one defect — rather than two
independent open problems.

**Proof economy.** A relation proved for $\mathfrak{V}$ over a commutative
ring $R$ with the **bar-involution** $\sigma$ (the structural setting —
*not* $\mathbb{C}$) descends to **both** the bar-even
(binding) and bar-odd ($\mathfrak{Q}_\beta$) parts from a single proof,
because the projections $x \mapsto x\pm\sigma x$ act additively. Formalised
in [`QOU.MassEndomorphism`](binding-qbeta-complex-volume.lean):
`invol_descent` (one ring identity $\Rightarrow$ both parity identities)
and `recurrence_invol_descent` (a three-term $\mathfrak{V}$-recurrence with
a bar-even multiplier $c$, $\sigma c = c$, yields the binding and
$\mathfrak{Q}_\beta$ recurrences at once — the `c_k`-ladder mechanism). The
$\mathbb{C}$/Re–Im picture forms the archimedean instance ($\sigma=$ complex
conjugation).

## Channel recurrences over categorical $R$, and the rotation between them

The two channels carry explicit three-term recurrences, stated in the same
generic setting (commutative ring $R$ with bar involution $\sigma$, never
$\mathbb{R}$ or $\mathbb{C}$; division-free via $\sigma q \cdot q = 1$):

- **even channel** (compact / binding / continuous $q$-Hermite):
  $H_{n+2} = 2x\,H_{n+1} - (1 - q^{n+1})\,H_n$ (`evenStep`);
- **odd channel** (non-compact / $\mathfrak{Q}_\beta$ / $q^{-1}$-Hermite),
  multiplied through by $q^{n+1}$:
  $q^{n+1}\,h_{n+2} = 2x\,q^{n+1}\,h_{n+1} + (q^{n+1} - 1)\,h_n$ (`oddStep`).

The **channel rotation** is proved (`rotation_step`). With a
formal rotation element $\iota \in R$, $\iota^2 = -1$ (the fibre-level
stand-in for $i$; `Complex.I` is only the archimedean instance downstream
of $\tau$), a sequence satisfies the odd step at $(q, x)$ **iff** its
$\iota$-rotation $n \mapsto \iota^n h_n$ satisfies the even step at the
bar-conjugated data $(\sigma q, \iota x)$ — the categorical form of the
Askey/Ismail–Masson identity $h_n(x \mid q) = i^{-n} H_n(ix \mid q^{-1})$
\cite{askey1989qhermite,ismail-masson1994}. Same eigenfunctions, rotated;
one recurrence, two channels.

The operator ("rotation matrix") statement is split by provability.
`eigencolumn_eq_overlap` proves generically that any eigencolumn of the
channel tridiagonal operator has orthogonal-polynomial entries. The
Leonard self-duality that would force those entries into the Askey–Wilson
family \cite{zhedanov1991,terwilliger2001} is carried as the conjecture
class `ChannelLeonardDuality`. The bound $\leftrightarrow$ free
deformation-path reading (endpoints of one Askey–Wilson family, with the
$\mathfrak{V}$-ladder riding one bar-even three-term multiplier) is carried as the
conjecture class `AWDeformationPath`, whose two-channel descent
`channel_ladders` is derived from `recurrence_invol_descent`. See the
companion remarks
[The channel rotation in the Askey scheme: same eigenfunctions rotated, different measures](#rem:channel-rotation-askey-lit) and
[Bound $\leftrightarrow$ free as a character-variety path: the deformation reading of $\mathfrak{V}$](#rem:complex-volume-character-variety-path).

**Archimedean specialisation.** The measured binding and $Q_\beta$ form the real and imaginary parts $\mathrm{Re}, \mathrm{Im}$ of the complex Bring-surface volume, valued in $\mathbb{R}$ (with $E_0 : \mathbb{R}$). This provides the archimedean readout of the generic complex-volume construction, acknowledged here.

Two further pieces of the operator picture are proved at the free
endpoint. First, the concrete $AW(3)$ realization: splitting the channel
tridiagonal operator into lowering, raising, and grading parts $L$, $R$, $Q$
(the shift-split of multiplication by $2x$ at the $q$-Hermite bottom), the
Zhedanov algebra degenerates to the $q$-oscillator relations

$$
Q R = q\,(R Q), \qquad L Q = q\,(Q L), \qquad L R - R L = (1 - q)\,Q,
$$

proved coordinatewise over generic $R$ (`chQR_rel`, `chLQ_rel`, `chLR_comm`),
with `chM_eigencolumn_iff` identifying the eigencolumns of $L + R$ with the
$q$-Hermite three-term rows; the odd channel satisfies the same relations at
$\sigma q$ by instantiation. Second, the **Casoratian mechanism** of the
$W$-sign test: two solutions of one three-term step transport their Casoratian
by $W' = -B\,W$ (`casoratian_step`), and along a bar-even constant-multiplier
ladder the channel Casoratian is *invariant* (`channel_casoratian_const`) — so
a measured drift of the physical channel Casoratian reads directly as the
$k$-dependence of the Askey–Wilson coefficient $B_k$. With $c_3^{\text{even}}$
now measured exactly (witness `qbeta-c3even-exact-sseries`), the decisive
$W_3$ sign test awaits only the $c_4$ rung pair.
