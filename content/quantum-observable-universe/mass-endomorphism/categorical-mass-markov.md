The categorical mass definition
([mass identity](#def:mass-identity)) descends to the
Iwahori--Hecke algebra in exactly three steps, each
categorically clean.  The result is that **single-level
categorical mass equals the absolute value of the Markov
trace**.

## Statement

**Proposition.**
*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
Frobenius--Hopf object $A = H_n(R, q)$ over a commutative ring $R$,
and let $\varrho \colon \mathbf{1} \to A$ be a closed cycle representing
the knot $\mathcal{K}$ with braid representative $\beta_\mathcal{K} \in B_n$.
Then the categorical mass ([mass identity](#def:mass-identity))
evaluated at a single brane level satisfies*

$$
  \mathfrak{m}_{q,\mathcal{K}}\big|_{\text{single level}}
  \;=\; \Bigl|\!\int_A\! \rho(\beta_\mathcal{K})\Bigr|,
$$

*where $\int_A : A \to R$ is the Jones--Markov trace, viewed as the
Frobenius integral on $A$.*

## Note — the modulus keeps only the bar-even shadow

The absolute value in
$\mathfrak{m}\big|_{\text{single level}} = \bigl|\int_A \rho(\beta_\mathcal{K})\bigr|$
retains only the **bar-even** ($\cosh$, real-$q$) component of the
Markov trace — the **mass / binding** channel. The **bar-odd**
($\sinh$, root-of-unity-$q$) component it discards is **not noise**:
it is the imaginary part of the complex fibre observable
$\mathfrak{V}$ (the QOU Neumann–Zagier volume,
$\mathfrak{V} = \mathfrak{E}_{\mathrm{bind}} + i\,\mathfrak{Q}_\beta$),
and equals the $\beta$-decay $Q$-value
$\mathfrak{Q}_\beta = \mathrm{Im}\,\mathfrak{V}$. Mass and
$\mathfrak{Q}_\beta$ are the two parities of one object
([`conj:binding-qbeta-complex-volume`](binding-qbeta-complex-volume.md)).
**Discipline:** taking $|\cdot|$ here is correct only when the mass
*magnitude* is all that is needed; any computation that also wants
$\mathfrak{Q}_\beta$, or that ties binding to decay, must keep the
**bar-odd shadow** (the root-of-unity evaluation), not collapse to the
modulus. This is *not* a complex $q_0$: at the observable level
$\mathrm{Im}(q_0) = 0$; the imaginary part is the *fibre-level*
($\sinh$/root-of-unity) shadow, a separate real observable.
