---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-019-531-the-brane-setup
section_title: "The Brane Setup"
section_number: 5.3.1
pages: 46-48
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
toc_source: outline
text_source: latex
latex_prose_ratio: 0.941
latex_coverage_ratio: 1.0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
To quantitatively test the feasibility of using a throat to evade the computational hardness of decoding, we need a specific example of this type of geometry. In string theory there is a standard way of producing throat geometries with the desired properties by stacking branes; for example D3 branes in type IIB string theory or M5 branes in M-theory. To realize the geometry [\[AdSsch\]](#AdSsch){reference-type="eqref" reference="AdSsch"} explicitly we would need a configuration of branes which is spherically symmetric and stable. Spherical symmetry is a bit inconvenient because branes in spherical configurations tend to collapse under their own tension unless there is something else supporting them. A simple thing we could do is start with the $AdS_3\times S^3\times T^4$ solution of IIB supergravity with RR flux, itself the near horizon limit of the $D1-D5$ system, and then wrap some $D3$ branes on the $S^3$. This throat would not be asymptotically Minkowski, but we could easily arrange for the curvature radius of the $AdS_3$ to be much larger than the curvature radius of the $AdS_5$ near the $D3$ branes. Rather than try to make this construction work in detail, we will instead consider a simpler setup in which the black hole has planar symmetry instead of spherical symmetry.

One of the best-known solutions of ten-dimensional IIB supergravity is the extremal planar black 3-brane [@Horowitz:1991cd], with metric $$\label{extbb}
ds^2=Z(r)^{-1/2}\left(-dt^2+d\vec{x}^2\right)+Z(r)^{1/2}\left(dr^2+r^2 d\Omega_5^2\right).$$ Here $$Z(r)=1+\left(\frac{R}{r}\right)^4,$$ and $R$ is a parameter of the solution. The string theory interpretation of this solution is that it gives the backreacted geometry in the presence of $N$ D3 branes, with $$R^4=4\pi g N \ell_s^4\sim N \ell_p^4$$ where $g$ is the string coupling, $\ell_s$ is the string length, and $\ell_p$ is the ten-dimensional Planck length. By looking at $Z(r)$ we see that this geometry indeed has the property that for $r\ll R$ it behaves like $AdS_5$ in Poincaré coordinates, times an extra $S^5$ of constant radius, while for $r\gg R$ it becomes ten dimensional Minkowski space.

To get something like a black hole down the throat we need to put this solution at finite temperature, and to get the entropy to be finite we need to compactify the spatial $\vec{x}$ directions. Although it will not be explicit in our equations, we will choose anti-periodic boundary conditions for the fermions around the compact dimensions.[^1] To add some temperature we just need to consider the non-extremal version of the solution [@Gubser:1996de]: $$\label{nonext}
ds^2=Z(r)^{-1/2}\left(-f(r)dt^2+d\vec{x}^2\right)+Z(r)^{1/2}\left(\frac{dr^2}{f(r)}+r^2 d\Omega_5^2\right),$$ where $Z(r)$ is now $$Z(r)=1+\lambda \left(\frac{R}{r}\right)^4,$$ with $$\lambda=\sqrt{1+\frac{1}{4}\left(\frac{r_0}{R}\right)^8}-\frac{1}{2}\left(\frac{r_0}{R}\right)^4$$ and $$f(r)=1-\left(\frac{r_0}{r}\right)^4.$$

To put the black hole far down the throat we clearly want $\frac{r_0}{R}\ll1$, and in this limit the entropy of the black hole is $$\label{ent}
S=\frac{\Omega_5 L^3r_0^3R^2}{4G}\sim \frac{L^3 r_0^3 R^2}{\ell_p^8}$$ and the temperature is $$\label{temp}
T=\frac{1}{\pi}\frac{r_0}{R^2}.$$ Here $\Omega_5$ is the volume of a unit $\mathbb{S}^5$ and $L$ is the periodicity of the $\vec{x}$ directions. In the same limit the ADM energy [^2] is $$E_{ADM}=\frac{\Omega_5L^3}{4\pi G}\left(R^4+\frac{3}{2}r_0^4\right).$$ One can check that when $r_0\to 0$ this reproduces the correct D3-brane tension. The energy above extremality is $$\label{eng}
E=\frac{3\Omega_5 L^3 r_0^4}{8 \pi G}\sim \frac{L^3 r_0^4}{\ell_p^8}.$$ It is straightforward to check that the instability encountered in Reissner-Nordstrom does not happen here; in fact we have $$\label{engent}
E=\frac{3}{2} S T,$$ so the energy will be bigger than the temperature until the black hole has Planckian area. We may then worry that the black hole evaporation time is independent of the intial entropy, as we worried with Reissner-Nordstrom, but there is now a new phenomenon which comes to the rescue.

[^1]: The reason for this choice is that compactifying with periodic boundary conditions preserves supersymmetry, which introduces an instability of the throat. Supersymmetry ensures there is no potential energy cost for separating the D3 branes that make up the throat. In CFT language the dual gauge theory is unable to pick a vacuum and its zero modes wander freely on its moduli space. Antiperiodic boundary conditions break supersymmetry and generate a potential that keeps the branes together. We thank Igor Klebanov and Juan Maldacena for discussions of this point.

[^2]: For an asymptotically flat geometry, in coordinates where the metric is $\eta_{\mu\nu}+h_{\mu\nu}$ with $h_{\mu\nu}$ small, the ADM energy is defined [@PhysRev.122.997] as $\lim_{r\to \infty}\frac{1}{16\pi G}\int dA n^{i}\left(\partial_j h_{ij}-\partial_i h^j_{\phantom{j}j}\right)$. Here the integral is over the $\mathbb{S}^5\times \mathbb{T}_3$ at infinity.
