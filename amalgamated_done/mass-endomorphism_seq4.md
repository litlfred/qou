<!-- FILE_START: complex-volume-intro.md -->
The mass endomorphism $\mathcal{M}$ carries more information than its real trace. Over $\mathbb{C}$, the projection defect $\mathrm{tr}_M\bigl((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M}\bigr)$ defines a single complex observable, the complex volume $\mathfrak{V}(K)$. Here, $\Pi_{\text{free}}$ is the factorized projector onto unlinked constituents. We define $\mathfrak{V}(K) = E_0\,\mathrm{tr}_M\bigl((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M}\bigr)$. This acts as the QOU analogue to the Neumann–Zagier complex volume $\mathbb{V}(K) = \operatorname{Vol}(K) + i\,\mathrm{CS}(K)$.

The framework's two nuclear observables serve as the two real shadows of $\mathfrak{V}$. Binding energy forms the real part ($\mathfrak{E}_{\mathrm{bind}} = \operatorname{Re}\mathfrak{V}$). This is the bar-even, $\cosh$, strong channel representing stable binding. The $\beta$-decay $Q$-value forms the imaginary part ($\mathfrak{Q}_\beta = \operatorname{Im}\mathfrak{V}$). This is the bar-odd, $\sinh$, weak channel representing unstable decay.

The unified reconstruction $\mathfrak{E}_{\mathrm{bind}} + i\,\mathfrak{Q}_\beta = \mathfrak{V}$ is formalized in Lean without `sorry`. The physical conjecture asserts that the measured binding and $Q$-value precisely equal these real and imaginary components under a shared normalization.

## Fibre-level caveat

At the archimedean, observable level, $\operatorname{Im}(q_0) = 0$. Binding and $\mathfrak{Q}_\beta$ are both real measured quantities. The complex structure exists strictly at the fibre level (pre-$\tau$). $\mathfrak{E}_{\mathrm{bind}}$ and $\mathfrak{Q}_\beta$ are real observable shadows of one complex fibre object under different archimedean evaluations (the real-$q$ volume channel versus the root-of-unity Chern–Simons channel). There is no "complex mass."

## Real shadow correspondence

This unified complex volume reframes the mass and $\beta$-decay narrative. We compute $\mathfrak{V}(K)$ once. Its real part supplies all binding energies; its imaginary part supplies all $Q$-values. They align aspect-by-aspect:

| aspect | real part $\operatorname{Re}\mathfrak{V}$ | imaginary part $\operatorname{Im}\mathfrak{V}$ |
|---|---|---|
| **observable** | binding energy $\mathfrak{E}_{\mathrm{bind}}$ | $\beta$-decay $Q$-value $\mathfrak{Q}_\beta$ |
| **bar-parity** | bar-even ($\sigma$-fixed, $x+\sigma x$) | bar-odd ($\sigma$-anti, $x-\sigma x$) |
| **eigenvalue function** | $\tfrac{q+q^{-1}}{2}=\cosh\lambda$ | $\tfrac{q-q^{-1}}{2}=\sinh\lambda$ |
| **archimedean evaluation** | real $q$ (hyperbolic) | root-of-unity $q$ ($\cosh \to \cos$, $\sinh \to i\sin$) |
| **Neumann–Zagier analogue** | $\operatorname{Vol}(K)$ | $\mathrm{CS}(K)$ |
| **physical character** | strong / stable / confining | weak / unstable / anti-binding |
| **open number** | binding $\Delta_\lambda$ gap | $\mathfrak{Q}_\beta$ $c_k$ residual |

Closing either column should mathematically close the other, as they constitute the real and imaginary parts of a single unclosed defect.
<!-- FILE_END: complex-volume-intro.md -->

<!-- FILE_START: binding-qbeta-complex-volume.md -->
**Conjecture (complex-volume unification of mass-binding and decay).**
*Binding and the $\beta$-decay $Q$-value are not two stories. They form
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
$\mathbb{V}(K) = \mathrm{Vol}(K) + i\,\mathrm{CS}(K)$.*

## The one object

Categorically — **no braid words**. For a confined knot $K$:

- $\mathcal{M} = \mathcal{M}(K) \in \mathrm{End}_{\mathbf{C}}(X_K)$
  forms the mass endomorphism of the object $X_K$ representing $K$ in
  the rigid monoidal category $\mathbf{C}$.
- $\mathrm{tr}_M : \mathrm{End}_{\mathbf{C}}(X_K) \to k$ provides the
  categorical Markov trace (the closed/categorical trace; AGENTS.md
  §7a — the fibre functor $\tau$ is a *different* object, never
  $\tau_M$).
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
([`prop:categorical-mass-markov`](#prop:categorical-mass-markov),
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
  ([`rem:block-multiplicativity-v-free`](../mass-theory/block-multiplicativity-v-free.md)).
  The $q$-deformed case remains class-axiomatized (conjectural).
- **Conjectural (the unification itself).** We conjecture that the physical binding
  and $\mathfrak{Q}_\beta$ construct the Re/Im of the **same** $\mathfrak{V}$
  at a single normalization.
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

## Computational corroboration (this PR)

The two channels really construct distinct real components of one object: the
$E_0\cdot|\Delta(\mathrm{net})|$ **net-route** (the bar-even, binding-like
$E_0\cdot\Delta(\mathrm{tr})$) provides a precision-ladder $c_2 \approx -8.0$,
whereas the canonical $c_2 = -1$ lives in the bar-odd $\mathrm{tr}_M$
**brane-tower** ladder
([`docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md`](../../../docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md),
witness `qbeta-ck-sseries-operator-match`). Two different real $c_2$'s for
the two parities perfectly align with Re/Im components of one complex
$c_2$.

## Corollary — one story, and one proof

Conditional on the unification, the framework's mass/binding chapter and
its $\beta$-decay chapter form **one derivation**: compute the complex
defect $\mathfrak{V}(K)$ once. Its real part yields every binding energy. Its
imaginary part yields every $Q$-value. The "$0.17\%$ $\mathfrak{Q}_\beta$
residual" and the binding $\Delta_\lambda$ gap become the *same* unclosed
object — the imaginary and real parts of one defect — rather than two
independent open problems.

**Proof economy.** A relation proved for $\mathfrak{V}$ over a commutative
ring $R$ with the **bar-involution** $\sigma$ (the structural setting —
*not* $\mathbb{C}$, per AGENTS.md §7c) descends to **both** the bar-even
(binding) and bar-odd ($\mathfrak{Q}_\beta$) parts from a single proof,
because the projections $x \mapsto x\pm\sigma x$ act additively. Formalised
sorry-free in [`QOU.MassEndomorphism`](binding-qbeta-complex-volume.lean):
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

The **channel rotation** is proved sorry-free (`rotation_step`). With a
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
[`rem:channel-rotation-askey-lit`](#rem:channel-rotation-askey-lit) and
[`rem:complex-volume-character-variety-path`](#rem:complex-volume-character-variety-path).

**Archimedean specialisation (§7c).** The measured binding and $Q_\beta$ form the real and imaginary parts $\mathrm{Re}, \mathrm{Im}$ of the complex Bring-surface volume, valued in $\mathbb{R}$ (with $E_0 : \mathbb{R}$). This provides the archimedean readout of the generic complex-volume construction, acknowledged here.
<!-- FILE_END: binding-qbeta-complex-volume.md -->

<!-- FILE_START: channel-rotation-askey-lit.md -->
The bar-even (binding, $\cosh$) and bar-odd ($\mathfrak{Q}_\beta$, $\sinh$) channels of the complex volume $\mathfrak{V}$ constitute a single Askey-scheme family evaluated through a rotation. Both the rotation and its limits are classical.

## Channel recurrences

The continuous $q$-Hermite polynomials $H_n(x \mid q)$ construct the proved basis of the binding kernel. Under simultaneous variable rotation $x \mapsto ix$ and bar involution $q \mapsto q^{-1}$, they yield the Ismail–Masson $q^{-1}$-Hermite polynomials:

$$
h_n(x \mid q) \;=\; i^{-n}\, H_n(ix \mid q^{-1}).
$$

The two channel recurrences are identical up to this rotation. We formalize this generically over a commutative ring $R$ equipped with a bar involution $\sigma$ and a formal rotation element $\iota$ satisfying $\iota^2 = -1$. The Lean declaration `rotation_step` (sibling to [`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume)) encodes this: a sequence satisfies the odd-channel step at $(q, x)$ if and only if its $\iota$-rotation satisfies the even-channel step at $(\sigma q, \iota x)$. The archimedean $i$ emerges only downstream of the functor $\tau$.

## Orthogonality measures

The shared recurrence does not imply a shared spectral measure. The asymmetry remains structural:

| | even channel (binding) | odd channel ($\mathfrak{Q}_\beta$) |
|---|---|---|
| polynomials | $H_n(x \mid q)$, $x = \cos\theta$ | $h_n(x \mid q)$, $x = \sinh t$ |
| locus | compact, $x \in [-1, 1]$ | non-compact, $x \in \mathbb{R}$ |
| measure | $q$-Plancherel weight (determinate) | indeterminate moment problem |
| at $q_0 > 1$ | does not exist archimedeanly | native regime |

At the substrate anchor $q_0 > 1$, the even-channel measure fails to form a probability law ([`prop:q-gaussian-obstruction-at-q0`](../mass-theory/q-gaussian-obstruction-at-q0.md)). This presents the Bożejko–Speicher positivity obstruction. The rotation is therefore irreducibly fibre-level, consistent with observable $\mathrm{Im}(q_0) = 0$. Measure asymmetry explains why parity projection left the binding error unchanged while the recurrence tie holds. A three-term recurrence is measure-independent, whereas a projection is not.

## Literature precedents

1. **Askey and Ismail–Masson**: The $q > 1$ continuation of continuous $q$-Hermite \cite{askey1989qhermite} provides the eigenfunction rotation \cite{ismail-masson1994}.
2. **The modular double**: The non-compact channel couples $q = e^{i\pi b^2}$ to $\tilde{q} = e^{-i\pi/b^2}$. Ponsot–Teschner Racah–Wigner coefficients for $U_q(\mathfrak{sl}(2,\mathbb{R}))$ \cite{ponsot-teschner2001} sit at the non-compact Askey–Wilson level. The map $b \leftrightarrow 1/b$ drives the $6j$-level rotation. This divides $\Phi_q$ (Faddeev, non-compact) from $\mathrm{Li}_2^q$ (Rogers, compact).
3. **Quantum modularity**: The Andersen–Kashaev state integral of a knot factors into a $q$-series and a $\tilde{q}$-series. The leading asymptotics trace $\mathrm{Vol} + i\,\mathrm{CS}$ \cite{garoufalidis-zagier-2024}. One complex object dictates two channel factorizations, mirroring the Neumann–Zagier structure \cite{neumann-zagier1985} that $\mathfrak{V}$ transports to binding and decay.

## Leonard pairs

Zhedanov's $AW(3)$ algebra \cite{zhedanov1991} embeds the rotation as an operator identity. It pairs two operators, each tridiagonal in the other's eigenbasis, with Askey–Wilson polynomials forming the overlap matrix. The generic statement—that any eigencolumn of the channel tridiagonal operator has orthogonal-polynomial entries—is proved as `eigencolumn_eq_overlap`. The self-duality that places the channel overlap into the Askey–Wilson family via Terwilliger's classification \cite{terwilliger2001} is axiomatized by the conjecture class `ChannelLeonardDuality`.

## Vertex-algebra shadow

Under the bar involution, the character side splits as a $\mathbb{Z}_2$-orbifold $V = V^+ \oplus V^-$. The involved characters form false theta functions, appearing as $(1,p)$ singlet log-VOA characters \cite{creutzig-milas2014}. Their quantum modularity tracks the disk-interior versus root-of-unity rotation, using the Lawrence–Zagier $\Psi$ operation established at the $W_\lambda$ keystone. This structure suggests a path to unify the lepton-tower $\Phi_q$ mechanism with the binding/decay model.
<!-- FILE_END: channel-rotation-askey-lit.md -->

<!-- FILE_START: complex-volume-character-variety-path.md -->
The interpolation between the bound and free projections of [`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume) constitutes a path. The bar-odd channel provides its holonomy. No structure beyond the deformation itself is required to rotate between the bound and free states.

## Endpoints as representations

The free projection $\Pi_{\text{free}}$ drops inter-constituent confining crossings, retaining only linking data. It constructs the abelian representation of the knot group. The bound object—the full braiding—constructs the discrete-faithful side. These define the two distinguished points of the character variety of $K$.

## Path integral reading

Neumann and Zagier defined the complex volume as the integral of a holomorphic $1$-form along the path in the character variety connecting these representations \cite{neumann-zagier1985}. Transported to $\mathfrak{V}$:

$$
\mathfrak{V} \;=\; \Phi(\text{bound}) - \Phi(\text{free}),
\qquad
\mathfrak{E}_{\mathrm{bind}} = \mathrm{Re}\mathfrak{V},
\quad
\mathfrak{Q}_\beta = \mathrm{Im}\mathfrak{V},
$$

where $\Phi$ acts as a potential on the deformation path. The endpoint difference of $\Phi$ equals the projection defect $\mathrm{tr}_M\bigl((\Pi_{\text{free}} - \mathbf{1}) \circ \mathcal{M}\bigr)$. Its bar-even part represents the volume (binding) channel. Its bar-odd part captures the phase accumulated along the path. This matches how the Chern–Simons invariant acts as the phase companion to hyperbolic volume, consistent with the state-integral factorization picture \cite{garoufalidis-zagier-2024}.

## Categorical carrier

Prior to archimedean evaluation (over a generic ring $R$ with a bar involution), the deformation parameter $t$ of a single Askey–Wilson tridiagonal family carries the path. At $t = 0$, the family sits at the $q$-Hermite bottom of the scheme. Here, all Askey–Wilson parameters vanish, and the orthogonality measure uses the $q$-Plancherel weight $W_\lambda$, representing the free side. At $t = 1$, it supplies the bound channel data.

This is formalized in the conjecture class `AWDeformationPath`. The class specifies the family, the $q$-Hermite free endpoint, the potential yielding $\mathfrak{V}$, and a single three-term ladder recurrence with a bar-even multiplier. The two-channel descent—where both the binding and $\mathfrak{Q}_\beta$ ladders satisfy the exact same recurrence—is a derived theorem (`AWDeformationPath.channel_ladders` via `recurrence_invol_descent`), rather than an assumption.

## Falsifiable consequences

The class predicts one decidable numerical signature: the binding and $\mathfrak{Q}_\beta$ channel ladders share a single bar-even three-term multiplier. Equivalently, the multiplier solved from the complex ladder $\mathfrak{V}_A$ has a vanishing bar-odd part. This probes the holomorphic connection.

The mechanism remains computationally confirmed. The Hopf-power tower $\mathfrak{V}_n = \mathrm{tr}_M\bigl((\sigma_1^2)^n\bigr)$ strictly follows a three-term recurrence with the bar-even multiplier $q^2 + q^{-2}$ (the continuous $q$-ultraspherical class). This exercises `recurrence_invol_descent` end-to-end. 

The physical identification—that the measured $c_k$-ladder exemplifies this mechanism—remains open, gated on the even-channel $c_3$. Along the isotope triples $({}^2\mathrm{H}, {}^3\mathrm{H}, {}^4\mathrm{He})$ and $({}^2\mathrm{H}, {}^3\mathrm{He}, {}^4\mathrm{He})$, the parity split of the log-trace binding proxy does not share one bar-even multiplier. This refutes that specific ladder construction, but leaves the underlying mechanism—confirmed at the fibre level by the Hopf tower—intact.
<!-- FILE_END: complex-volume-character-variety-path.md -->

<!-- FILE_START: color-spacetime-s5-factorization.md -->
**Proposition (Color and spacetime are orthogonal factors of the Bring Galois group).**
*Let $K$ be a Bring-embeddable knot, evaluated through the categorical Markov trace $\mathrm{tr}_M$ on the Hecke algebra $H_2(q) \oplus H_3(q)$. The $2+3=5$ irreducible representations constitute the Bring fivefold. Bring's five homogeneous coordinates split as spacetime $(x_0, x_1)$ and color $(x_2, x_3, x_4)$. The substrate Galois group $S_5$ contains the block-diagonal product $S_2 \times S_3$. Then:*

1. *The factorization $S_2 \times S_3 \hookrightarrow S_5$ acts faithfully.*
2. *The color factor $S_3$ fixes every spacetime coordinate. The spacetime factor $S_2$ fixes every color coordinate. The two sectors remain orthogonal.*
3. *Every additive homomorphism from the connected phase parameter $\mathbb{R}$ to a finite group is trivial.*

## A single trace object

The embeddable strand counts dictate a single trace algebra $H_2(q) \oplus H_3(q)$ carrying $2+3=5$ irreducible representations ([`prop:cohomological-embedding`](#prop:cohomological-embedding)). These match Bring's five homogeneous coordinates, partitioned into a rank-two spacetime block and a rank-three color block ([`brings-qou-4tuple`](../brings-surface/brings-qou-4tuple.md)). We record the color content of an embedded photon as an element of $H_3(q)$, where the generators $\sigma_0, \sigma_1$ serve as the color axes ([`knot-basis-color-content`](../brings-surface/knot-basis-color-content.md)). Color therefore provides a grading on the trace algebra itself, rather than a separate object.

The substrate symmetry $S_5$ acts on all five coordinates. Its block-diagonal subgroup $S_2 \times S_3$ permutes spacetime and color separately. The $S_3$ permutes the three color sheets while preserving spacetime ([`color-sector-coords`](../brings-surface/color-sector-coords.md), [`rem:chirality-trefoil`](#rem:chirality-trefoil)). The $S_2$ permutes the two spacetime coordinates while preserving color. Parts (1) and (2) formalize this. The product embeds faithfully, and each factor fixes the opposing sector pointwise. Color and spacetime function as independent coordinates on a single object. They couple only through $S_5$ elements outside $S_2 \times S_3$, which rotate spacetime indices into color indices.

## Discreteness

Part (3) enforces rigidity on the continuous sector. The connected group $\mathbb{R}$ is divisible, so any homomorphism to a finite group $G$ vanishes. For each $x$, $f(x) = f\big(|G| \cdot \tfrac{x}{|G|}\big) = |G| \cdot f(\tfrac{x}{|G|}) = 0$, because $|G| \cdot g = 0$ for every $g \in G$. A continuous winding parameter cannot carry a finite-group (e.g. $\mu_5$) character. Physically, this dictates that the continuous trace phase does not constitute the discrete color charge ([`rem:mass-modulus-em-phase-color-grading`](#rem:mass-modulus-em-phase-color-grading)).

## Lean formalism

These claims are formalized without `sorry` in [`QOU.MassEndomorphism`](color-spacetime-s5-factorization.lean) via `spacetime_color_card`, `colorSpacetimeEmbed_injective`, `color_fixes_spacetime`, `spacetime_fixes_color`, and `winding_hom_to_finite_trivial`. The construction is generic. The embedding and divisibility arguments rely strictly on combinatorial data, requiring no archimedean input.
<!-- FILE_END: color-spacetime-s5-factorization.md -->

<!-- FILE_START: mass-modulus-em-phase-color-grading.md -->
The factorization of [`prop:color-spacetime-s5-factorization`](#prop:color-spacetime-s5-factorization) fixes how the three observables of a Bring-embeddable knot sit on the single trace scalar $\mathrm{tr}_M$ and its trace algebra $H_2(q)\oplus H_3(q)$.

## Three readings of one trace

We write the trace scalar in polar form:
$$
  \mathrm{tr}_M \;=\; \lVert\mathrm{tr}_M\rVert\,\exp\!\big(i\,\arg\mathrm{tr}_M\big).
$$
This forms the multiplicative companion of the additive complex-volume reconstruction $\operatorname{Re}\mathfrak{V}+i\operatorname{Im}\mathfrak{V}=\mathfrak{V}$ ([`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume)). We then have:

| reading | quantity | sector | character |
|---|---|---|---|
| **mass** | modulus $\lVert\mathrm{tr}_M\rVert$ | both | nonnegative magnitude |
| **electromagnetism** | argument $\arg\mathrm{tr}_M$ | spacetime / $S_2$ | continuous $U(1)$ |
| **color** | $S_3$ irrep grading | color / $S_3$ | discrete |

Mass evaluates the magnitude that survives both sectors. The argument evaluates the continuous $U(1)$ framing/Chern–Simons phase. This provides the $\operatorname{Im}\mathfrak{V}$ channel, picked up as the ribbon twist $q^{2w\,c(\lambda)}$ on a framed knot of writhe $w$ ([`bar-parity-split`](../mass-theory/bar-parity-split.md)). It lives in the spacetime block, where we read it as the electromagnetic phase. Color provides the discrete grading of the algebra element across the $H_3(q)$ representations, before the trace collapses it to a scalar.

## Color is not the phase

The color factor $S_3$ fixes the spacetime coordinates. The spacetime factor $S_2$ fixes the color coordinates ([`prop:color-spacetime-s5-factorization`](#prop:color-spacetime-s5-factorization), parts 1–2). Therefore, color and electromagnetism form independent coordinates. The discrete color charge is not a function of the continuous phase, and conversely. The rigidity in part $3$ of that proposition makes this non-coincidence sharp. A continuous winding argument cannot factor through a finite group such as $\mu_5$. Thus, $\arg\mathrm{tr}_M$ remains structurally barred from being a color character.

The two remain nonetheless faces of one substrate. The Galois group $S_5$ properly contains $S_2\times S_3$. Its remaining generators carry spacetime indices into color indices. An electromagnetic-to-color relation therefore forms an $S_5$ statement, realized by those off-block generators, not a relation internal to the $U(1)$ phase. Mass, electromagnetism, and color form one trace object read on its modulus, its spacetime phase, and its color grading.

## Archimedean realization

The polar split provides the archimedean reading. The modulus and argument require the realization of the trace over $\mathbb{C}$, on the far side of the substrate-to-archimedean wall. The structural content of [`prop:color-spacetime-s5-factorization`](#prop:color-spacetime-s5-factorization)—the faithful $S_2\times S_3\hookrightarrow S_5$ embedding, the orthogonality of the two sectors, and the divisibility rigidity—is generic and requires no such realization.

## Relation to the literature

The individual ingredients form classical results. The imaginary partner of a hyperbolic volume forms a Chern–Simons invariant (Neumann–Zagier \cite{neumann-zagier1985}). The colored-Jones asymptotics realize this complex volume at roots of unity (Volume Conjecture \cite{kashaev1997, murakami-murakami2001}). The Jones polynomial forms a Chern–Simons expectation value whose framing dependence produces the $U(1)$ phase (Witten \cite{witten1989}, Reshetikhin–Turaev \cite{reshetikhin1991}). The complexified continuation of the phase forms Witten \cite{witten2011}, and the bar-involution structure of the root-of-unity asymptotics forms the quantum-modularity of Zagier \cite{zagier2010}. The quantum dilogarithm controlling the asymptotics forms Faddeev–Kashaev \cite{faddeev1994}.

Read against this work, two of our identifications constitute recombinations and two are specific to this framework. The reading *modulus/argument = volume/Chern–Simons* and the placement of the argument as a $U(1)$ framing phase restate the cited results. The identification of the **modulus with mass** $\lVert\mathrm{tr}_M\rVert$ and of **color with the $S_3\subset S_5$ representation grading of the Bring quintic's Galois group** are our own. The literature offers the nearby $A_5$ / $S_5$ flavor and modular-flavor symmetries rather than this trace-algebra grading. Our contribution forms the group-theoretic statement that these three readings are orthogonal sectors of one trace object, alongside the rigidity barring the continuous phase from being the discrete color charge.

## Classical antecedents of the involutive reading

Resolving one object into observables under an involution is a recurring structure. Four classical instances frame ours:

- **Frobenius–Schur indicator.** The character involution $\chi\mapsto\chi(g^{-1})$ \cite{frobenius-schur1906}—the bar-involution $q\mapsto q^{-1}$ on the Hecke side—sorts every irreducible representation as real, quaternionic, or complex. The bar-even (binding, $\cosh$) and bar-odd ($\beta$-decay, $\sinh$) channels construct the rank-one shadow of this trichotomy on the trace.
- **Modular conjugation.** The Markov trace forms a trace on a finite von Neumann algebra \cite{jones1985}. Every such algebra carries the Tomita–Takesaki modular conjugation $J$ and modular operator $\Delta$ \cite{takesaki1970}. The observable elements are the $J$-fixed (self-adjoint) ones, and $a=\tfrac12(a+a^*)+\tfrac12(a-a^*)$ forms the algebra-level bar-parity split. The polar reading (mass $=\lVert\mathrm{tr}_M\rVert$, phase $=\arg\mathrm{tr}_M$) provides its modulus–modular-flow form.
- **Weil operator.** On a polarized Hodge structure, the Weil operator \cite{weil1958} supplies the complex structure packaging real harmonic periods into a polarized complex period. The complex volume $\operatorname{Vol}+i\,\mathrm{CS}$ \cite{neumann-zagier1985} provides such a period, and $H^1(\mathrm{Bring})=2W$ forms such a structure—the Hodge-theoretic home of the complex-volume half.
- **Conjugate-variable amplitude.** The oscillator amplitude $a=q+ip$ combines a canonically conjugate pair through the symplectic complex structure, with $\lVert a\rVert^2$ the energy and $\arg a$ the phase.

In physics, this reading follows the **complex-energy / resonance** tradition. A state forms a complex pole $\mathfrak{E}=\mathfrak{m}-i\Gamma/2$ (Gamow \cite{gamow1928}, Breit–Wigner \cite{breit-wigner1936}) whose real part gives mass and whose imaginary part gives decay width. The bound sector lies on the conjugation-fixed real axis, and the optical theorem ties the imaginary part to the total decay rate. The Kramers–Kronig dispersion relations \cite{kronig1926} lock the reactive (real) and absorptive (imaginary) parts of one causal response. There, the involution is complex conjugation / time reversal. Here, the bar-involution $q\mapsto q^{-1}$ plays that role at the fibre level. We claim not the involutive reading itself, but its realization on the categorical knot trace, where $\operatorname{Im}(q_0)=0$ at the archimedean level renders the two parts separately real observable shadows.
<!-- FILE_END: mass-modulus-em-phase-color-grading.md -->
