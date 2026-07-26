Let $(W, S)$ be a Coxeter system and $s_i, s_j$ a generator pair with
$m_{ij} = 3$ (respectively $m_{ij} = 2$). Then

$$
[s_i, s_j, s_i] \text{ is reduced}
\;\Longleftrightarrow\;
s_i \neq s_j
$$

(respectively $[s_i, s_j]$ is reduced $\Leftrightarrow s_i \neq s_j$).

The forward direction is elementary. For the converse the reflection
cocycle is used quantitatively: pairwise-distinct reflections $t$ with
cocycle value $\eta(w, t) = 1$ bound the length of $w$ from below,
because each such reflection occurs in the inversion sequence of any
reduced word for $w$. The inversion sequence of the cell word is
computed in closed form — $[\,s_j,\; s_i s_j s_i,\; s_i\,]$ at
$m_{ij} = 3$, the first entry collapsing by the braid relation, and
$[\,s_i,\; s_j\,]$ at $m_{ij} = 2$ — and simple-distinctness makes its
entries pairwise distinct, forcing $\ell \geq$ the word length.

Consequently the parabolic transversals, and with them the braid and
far-commutation relations on the length-rule module, require only
$s_i \neq s_j$ per pair: nothing about lengths or words survives in the
residue. What remains of Tits faithfulness, per generator pair, is
exactly injectivity of the simple-reflection map — the point where the
geometric representation classically enters.
