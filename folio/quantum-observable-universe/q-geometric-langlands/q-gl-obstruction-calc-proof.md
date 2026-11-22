**Item (1).**
The $q$-flatness equation is $\nabla_q^2 = (q-1)\mathcal{F}_q$ ([q-flat connection](#def:q-flat-connection)). Its intrinsic part $\mathcal{F}_q^{\mathrm{intr}}$ is a class in $HH^2(\mathcal{U}_q, \mathrm{Ad})$. HKR alone relates polyvector fields to Hochschild cohomology; it does not identify $HH^2(\mathcal{U}_q, \mathrm{Ad})$ with $H^2(\mathcal{S}, \mathbb{G}_m)$. That identification is hypothesis (H-HKR), under which $\Theta(\mathcal{F}_q^{\mathrm{intr}}) = \kappa_0 = e(\xi)$ ([Kummer filtration](#rem:kummer-filtration-obstruction)). Since $\Theta$ is injective, $\mathcal{F}_q^{\mathrm{intr}} \neq 0$ whenever $\kappa_0 \neq 0$.

**Item (2).**
$q$-flatness is the vanishing of the connection-dependent part $\mathcal{F}_q^{\mathrm{conn}}$, while $\kappa_0$ determines the intrinsic part $\mathcal{F}_q^{\mathrm{intr}}$ (item 1). The two are separate, so $\kappa_0 \neq 0$ does not prevent $q$-flatness; it only makes the intrinsic curvature non-zero. The lifting requirement is the [quantum lifting condition](#def:yekutieli-lifting-condition): lifting from level $n$ needs $\kappa_n = 0$, and $\kappa_n \equiv \kappa_0 \pmod n$, which gives $\kappa_0 \in n\,H^2(\mathcal{S}, \mathbb{G}_m)$.

**Item (3).**
By (H-tr), $\mathrm{tr}$ induces an isomorphism $H^2(\mathcal{S}, \mathbb{G}_m)/n \cong \mathbb{Z}/n$ sending $\kappa_0 \bmod n$ to $\chi(A) \bmod n$. So $\kappa_0 \bmod n = 0$ if and only if $n \mid \chi(A)$. Without (H-tr) the trace alone would not determine the class. The complementary subgroup structure $\kappa_n = \kappa_0 + \delta_n$ prevents cancellation.

**Item (4).**
The set $\{n : n \mid \chi(A)\}$ has exactly $d(|\chi(A)|)$ elements, where $d$ is the divisor function. This set is finite. Its complement in $\mathbb{Z}_{>0}$ has density $1$. $\square$

