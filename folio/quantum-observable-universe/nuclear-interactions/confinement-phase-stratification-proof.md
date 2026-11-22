*Proof.*
*Claim (1)—Openness.*
*Let $S := \{(q, X) : \forall i,\ 0 < g_i(q, X)\}$. Each set $\{0 < g_i\}$ is open because $g_i$ is continuous, and $I$ is finite, so $S$ is open. $\Omega(P)$ is the image of $S$ under the projection $(q, X) \mapsto q$, which is an open map. Hence $\Omega(P)$ is open.*

*Claim (2)—Constancy on a phase.*
*Fix $\lambda$. Let $U := \{q : u^*_\lambda(q) > 0\}$ and $V := \{q : s_\lambda(q) > 0\}$; both are open by continuity. Strict complementarity gives $C \subseteq U \cup V$. If $C$ met both $U$ and $V$, then, $C$ being connected, it would meet $U \cap V$ at some $q$; there $u^*_\lambda(q)\, s_\lambda(q) > 0$, contradicting complementarity. So either $u^*_\lambda > 0$ on all of $C$, or $u^*_\lambda > 0$ nowhere on $C$. This holds for every $\lambda$, so $\mathcal{S}^*(P, q)$ is the same set for every $q \in C$, and so is its size $\mu(P, q)$. $\square$*
