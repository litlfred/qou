**Conjecture (surreal limit transfer).** There is an $\omega$-evaluation
$\mathrm{ev}_\omega : \mathbb{R}^{\mathbb{N}} \to \mathbf{No}$ of real
sequences, sending constants to their embedded reals, respecting
pointwise addition and multiplication, transferring eventual pointwise
domination to the surreal order, and evaluating every convergent
sequence infinitesimally close to its limit:

$$
  a_n \to L
  \quad\Longrightarrow\quad
  \mathrm{ev}_\omega(a) - L \in \mathfrak{m},
  \qquad
  \mathrm{st}\bigl(\mathrm{ev}_\omega(a)\bigr) = L .
$$

Here $\mathfrak{m}$ is the infinitesimal ideal of the finite valuation
ring ([valuation ring of finite surreals](#rem:valuation-ring-finite-surreals))
and $\mathrm{st}$ the [standard-part map](#def:standard-part-functor).

This is the block-level home for the "move analytic $\to$ surreal"
operation: an analytic *limit statement* becomes a surreal
*equality up to an infinitesimal* — and, after $\mathrm{st}$, an exact
equality. Two consequences are **derived, fully proved**, from the
hypotheses of the conjecture:

1. *Limits are computed by* $\mathrm{st} \circ \mathrm{ev}_\omega$
.
2. *Limit comparison*: if $a_n \le b_n$ eventually and both converge,
   then $\lim a_n \le \lim b_n$
 — the eventual inequality is
   transferred to a single surreal inequality at $\omega$ and the
   archimedean conclusion recovered by the proved monotonicity of
   $\mathrm{st}$. The classical strict-inequality collapse is visible
   structurally: $\mathrm{ev}_\omega(a) < \mathrm{ev}_\omega(b)$ is
   compatible with equal standard parts, so only $\le$ survives the
   wall.

## Epistemic status

The conjecture is stated as a precise hypothesis with **no
proof** — it is open. For the concrete surreals the
evaluation exists model-theoretically: Robinson's ultrapower supplies
one \cite{robinson1966}, and the Berarducci–Mantova identification of
surreals with transseries/germs \cite{berarducci-mantova2018} supplies the
canonical one for the definable-germ class (evaluation of the germ at
$\omega$). Neither construction is available from the axiomatised
surreal-field interface alone, which is exactly why the block is a
conjecture rather than a theorem: what is conjectural is the
*compatibility package* on the abstract interface, not the existence
of some such map in set theory.

## Relation to resummation

For a *convergent* sequence, $\mathrm{st} \circ \mathrm{ev}_\omega$ is
ordinary summation. For a *divergent Gevrey-1* asymptotic series the
same composite, applied to the Berarducci–Mantova evaluation of the
associated transseries, is the median resummation — the identification
recorded in [st is median resummation](#rem:st-is-median-resummation).
The conjecture is therefore the convergent-sector base case of the
resummation dictionary: it fixes the normalisation that any
median-resummation extension must restrict to.
