## Kernel invariance and strict cost drop across $\mathcal{G}_{\mathrm{phys}}$

Each of the eleven exponent vectors $g \in \mathcal{G}_{\mathrm{phys}}$ satisfies $A_0 g = 0$ by direct evaluation on the two rows of $A_0$, so adding any multiple of the rows of $A_0$ to the motif cost vector leaves $c \cdot g$ unchanged. Under the five chamber inequalities $0 < B_d$, $B_d < B_h$, $B_d < B_t$, $2 B_t < B_\alpha$, and $2 B_h < B_\alpha$, positivity of $B_t$ and $B_h$ follows by transitivity from $0 < B_d$. The eleven cost drops $c \cdot g$ then decompose as positive sums inside $R$:

- $B_d > 0$, $B_h - B_d > 0$, $B_t - B_d > 0$, $B_\alpha - 2 B_t > 0$, and $B_\alpha - 2 B_h > 0$ are the five facet generators directly;
- $B_\alpha - B_t = (B_\alpha - 2 B_t) + B_t > 0$ and $B_\alpha - B_h = (B_\alpha - 2 B_h) + B_h > 0$;
- $B_\alpha - 2 B_d > B_\alpha - 2 B_t > 0$, $B_\alpha - B_d - B_t > B_\alpha - 2 B_t > 0$, and $B_\alpha - B_d - B_h > B_\alpha - 2 B_h > 0$ follow from $B_d < B_t$ and $B_d < B_h$;
- for $x_t x_h \to x_d x_\alpha$, doubling the difference $B_\alpha - B_t - B_h$ yields $(B_\alpha - 2 B_t) + (B_\alpha - 2 B_h) > 0$, whence $B_\alpha - B_t - B_h > 0$ in the torsion-free ordered group $R$, and adding $B_d > 0$ gives $B_\alpha + B_d - B_t - B_h > 0$.

Whenever any feasible integer vector $u$ differs from $u^*$ by a nonnegative integer combination $\sum_r n_r g_r$ of positively oriented Graver moves, linearity of the pairing gives $c \cdot u - c \cdot u^* = \sum_r n_r (c \cdot g_r) \ge 0$, certifying global integer optimality on the fiber $A_0 u = (Z, N)$.

## Monomial normal forms, Hoyle orientation, and capacitated shells

Applying $\mathcal{G}_{\mathrm{phys}}$ to $x_p^2 x_n^3$ fires $x_p x_n \to x_d$, $x_n x_d \to x_t$, and $x_p x_t \to x_\alpha$ in three steps, terminating at $x_\alpha x_n$; none of the eleven leading monomials divides $x_\alpha x_n$ because $x_\alpha$ appears in no leading monomial of $\mathcal{G}_{\mathrm{phys}}$. The normal forms of $x_p^6 x_n^6$, $x_p^7 x_n^7$, $x_p^4 x_n^5$, and $x_p^5 x_n^4$ follow by the same finite reduction.

On $A_{\mathrm{Hoyle}} = (4, 8, 12)$, the vectors $g_{{}^8\mathrm{Be}} = (-2, 1, 0)$ and $g_{\mathrm{Hoyle}} = (3, 0, -1)$ satisfy $4(-2) + 8(1) = 0$ and $4(3) - 12(1) = 0$, with cost drops $c_{{}^8\mathrm{Be}} - 2 c_\alpha > 0$ and $3 c_\alpha - c_{{}^{12}\mathrm{C}} > 0$. Finally, on any capacitated shell fiber $u_s + w_s = C_s$ with $C_s \ge 1$, vanishing of both $u_s$ and $w_s$ would contradict $C_s \ge 1$, so no intermediate full or empty shell can block an adjacent promotion chain $u_{s+1} w_s \to u_s w_{s+1}$.
