Let $(W, S)$ be a Coxeter system with length function $\ell$, let
$\omega = (s_{i_1}, \dots, s_{i_k})$ be any word in the generators (not
necessarily reduced), and let $t$ be a reflection of $W$ with
$\ell(\pi(\omega)\, t) < \ell(\pi(\omega))$, where $\pi(\omega)$ denotes
the product of the word. Then some single letter of $\omega$ can be
deleted: there is an index $j < k$ with

$$
\pi(\omega)\, t \;=\; \pi(\omega \setminus j),
$$

where $\omega \setminus j$ is the word with its $j$-th letter erased.

The proof is the classical reflection-cocycle construction. Each
generator $s$ acts on $W \times \mathbb{Z}/2$ by
$(w, \varepsilon) \mapsto (s w s,\; \varepsilon + [w = s])$; these
involutions satisfy the Coxeter relations because the inversion sequence
of the doubled braid word consists of two identical halves, so every
$\mathbb{Z}/2$ parity count cancels. The resulting homomorphism
$W \to \mathrm{Perm}(W \times \mathbb{Z}/2)$ makes the parity
$\eta(w, t)$ of the number of occurrences of $t$ in the right inversion
sequence independent of the chosen word for $w$. The cocycle law gives
$\eta(t, t) = 1$ for every reflection, hence
$\eta(wt, t) = 1 + \eta(w, t)$, and a length descent forces
$\eta(w, t) = 1$; a positive parity locates an occurrence of $t$ in the
inversion sequence, and deleting that letter realises the product. No
induction on length and no reduced-word hypothesis is needed.
