*Lean sibling: $\mathbb{N}$ genus combinatorics and $\mathbb{C}$ for $\zeta_5$ (CLAUDE.md §7c — the Gauss sum is the archimedean specialisation; the embedding combinatorics stay over $\mathbb{N}$).*

**Proposition (trefoil $+$ cinquefoil channel).** *In Bring's genus-$4$ Seifert
fibre $\Sigma_4$ — whose automorphism group is $\mathrm{Aut}(B) = S_5$, permuting
the five roots the Bring radical resolves — the chiral channel and the $\zeta_5$
symmetry are carried by two **distinct** torus knots, linked by the ambient $S_5$:*

- *the **chiral channel** is the **trefoil** $T_{2,3}$, of Seifert genus
  $g(T_{2,3}) = :val[bring_g_trefoil]{precision=0, witness=folio-assistant/computations/bring-trefoil-cinquefoil-channel.witness.json}$
  — the colour-tube cubic's three sheets $(r,g,b)$ with $B_3 \twoheadrightarrow H_3$
  branch monodromy, i.e. the signed-content-zero block $V_{(2,1)}$
  ($c_\lambda = 0$, the $q$-Dirac kernel);*
- *the **$\zeta_5$ carrier** is the **cinquefoil** $T_{2,5}$, of Seifert genus
  $g(T_{2,5}) = :val[bring_g_cinquefoil]{precision=0, witness=folio-assistant/computations/bring-trefoil-cinquefoil-channel.witness.json}$
  — the hyperelliptic quintic $\mathcal{X}_5 \colon y^2 = x^5 - 1$
  ([`def:hyperelliptic-quintic`](#def:hyperelliptic-quintic)) **embedded** (not
  covered) by the first Lagrange resolvent $w_1$ of the cyclic
  $\mathbb{Z}_5 \subset S_5$, its five branch points one $\mathbb{Z}_5$-orbit
  $\{1, \zeta_5, \dots, \zeta_5^4\}$ ([`prop:x5-z5-automorphism`](#prop:x5-z5-automorphism)).*

*Both embed in $\Sigma_4$ — genus $1$ and $2$ are $\le g(\Sigma_4) =
:val[bring_sigma4_genus]{precision=0, witness=folio-assistant/computations/bring-trefoil-cinquefoil-channel.witness.json}$, within the complete embeddable
list $\{(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)\}$ of
[`prop:torus-embeddable-complete`](#prop:torus-embeddable-complete) — and they
are distinct. The quadratic Gauss sum over the cinquefoil's $\mathbb{Z}_5$-orbit,*

$$
  g \;=\; \sum_{k=0}^{4} \zeta_5^{\,k^2},
  \qquad g^2 = 5,
  \qquad g = +\sqrt5,
$$

*is the unique source of $\zeta_5$'s irrationality over $\mathbb{Q}$, carried by
the resolvent $w_1$ (numerically $g \approx :val[bring_gauss_sum_sqrt5]{precision=5, witness=folio-assistant/computations/bring-trefoil-cinquefoil-channel.witness.json}$).
The chiral residue's only available irrational scale on this configuration is
therefore $\sqrt5$, and its Bring constant is
$1/\sqrt5 \approx :val[bring_inv_sqrt5]{precision=5, witness=folio-assistant/computations/bring-trefoil-cinquefoil-channel.witness.json}$.*

## Two torus knots, not one fibre

The phrasing "the chiral channel lives on the Bring chiral fibre with $\zeta_5$
symmetry" conflates two distinct structures. The colour-tube cubic
([`rem:color-tube-cubic`](#rem:color-tube-cubic)) is a **$3$-fold** datum — three
sheets, $B_3 \twoheadrightarrow H_3$, the trefoil. The $\zeta_5$ is a **$5$-fold**
datum — a cyclic subgroup of $S_5$, realised by the cinquefoil. They are not the
same knot, and the $5$-fold is *not* a covering of the $3$-fold: it is a second
torus knot embedded in the *same* $\Sigma_4$, and the ambient $S_5$ relates the
two. The $\sqrt5$ does not come from the cubic fibre; it comes from the
$\mathbb{Z}_5$-orbit Gauss sum carried by the resolvent $w_1$ that embeds the
quintic.

| structure | torus knot | Seifert genus | carried by |
|---|---|---|---|
| chiral channel ($3$-fold) | trefoil $T_{2,3}$ | $1$ | colour-tube cubic, $B_3 \twoheadrightarrow H_3$ |
| $\zeta_5$ symmetry ($5$-fold) | cinquefoil $T_{2,5}$ | $2$ | quintic $\mathcal{X}_5$ via the $w_1$ resolvent |

Both rows sit inside the single genus-$4$ fibre $\Sigma_4$; the third
column is exactly the descending chain
$g(T_{2,3}) = 1 < g(T_{2,5}) = 2 < g(\Sigma_4) = 4$.

## Relation to the H$_2$S residual

This proposition is the **provable geometric scaffold** beneath the H$_2$S
bond-angle conjecture ([`conj:h2s-angle-s3-braid-holonomy`](../molecular-construction/h2s-angle-s3-braid-holonomy.md)),
which observes the residual opening $\Delta\theta_{\mathrm{H_2S}}$ takes the Bring
$1/\sqrt5$ residual-mixing form. The scaffold fixes *which* $\sqrt5$ is available
(the quintic Gauss sum of the cinquefoil, $g^2 = 5$) and *why* the chiral channel
can see it (it is the trefoil sharing $\Sigma_4$ with the cinquefoil, $S_5$-linked).
What remains conjectural is only the **exact normalisation** — that the
$\zeta_5$-residue of the chiral $3p_z$ braid returns *precisely* the coefficient
$1/\sqrt5$ (equivalently, that the archimedean root of $g^2 = 5$ enters with the
observed weight). That monodromy/Reshetikhin–Turaev evaluation at $\zeta_5$ is the
conjecture's open content; the discrete scaffold here is established.

## Lean structure

`QOU.BringChiralCinquefoil` (sibling `bring-trefoil-cinquefoil-channel.lean`):

- `bring_trefoil_cinquefoil_channel` — the genera $g(T_{2,3}) = 1$,
  $g(T_{2,5}) = 2$, both $\le 4$, and $g(T_{2,3}) \ne g(T_{2,5})$ (two distinct
  knots in $\Sigma_4$). **Sorry-free** (`decide`).
- `zeta5_pow_five` — $\zeta_5^5 = 1$, the $5$-fold symmetry. **Sorry-free**
  (matching [`prop:x5-z5-automorphism`](#prop:x5-z5-automorphism)).
- `quintic_gauss_sum_sq_eq_five` — $\bigl(\sum_k \zeta_5^{k^2}\bigr)^2 = 5$.
  **Sorry-free** — proved from $\zeta_5$ primitivity
  (`Complex.isPrimitiveRoot_exp`) and the cyclotomic relation
  $1+\zeta_5+\zeta_5^2+\zeta_5^3+\zeta_5^4 = 0$ (`geom_sum_eq_zero`), reducing
  $\zeta_5^9 \mapsto \zeta_5^4$, $\zeta_5^{16} \mapsto \zeta_5$ and closing
  $g^2 - 5 = (4\zeta_5^3+8)(\zeta_5^5-1) + 4(1+\zeta_5+\zeta_5^2+\zeta_5^3+\zeta_5^4)$
  by `linear_combination` (\cite{washington1997} is the classical reference for
  the value). The archimedean *sign* $g = +\sqrt5$ — not the value $g^2 = 5$ — is
  the only deferred part, and it is the conjecture's open normalisation content.
