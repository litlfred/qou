---
doc_id: arxiv-2211.13362v2
doc_title: "Double-slit experiment revisited"
section_id: sec-002-trajectories-for-the-dse
section_title: "Trajectories for the DSE"
section_number: null
pages: 3-5
source_pdf: 2211.13362v2.pdf
source_sha256: 3becbeaa1135d2e1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.895
---
Bohmian mechanics (also called the de Broglie-Bohm theory or pilot-wave theory) is a theory describing point particles moving along trajectories that grounds the formalism and predictions of standard quantum mechanics [@BohmHiley; @HollandBook; @DurrTeufel; @DGZOperators]. For a single-particle with position $\vb{R}$ and mass $m$, the dynamics is given by the guidance equation $$\label{eq:guide}
    \dot{\vb{R}}(t)=\frac{\hbar}{m}\kern 0.1em\Im\!\left[\!\frac{\pmb{\nabla}\psi\big(\vb{R}(t),t\big)}{\psi\big(\vb{R}(t),t\big)}\!\right]\!,$$ where $\psi(\vb{r},t)$ is the wave function satisfying Schrödinger's equation with an external potential $V(\vb{r},t)$. The wave function never collapses in this theory. Here, the "wave/particle duality" of quantum mechanics is resolved in a trivial way: both a wave *and* a particle are present.

The motion of the particle is deterministic, i.e., given its initial position $\vb{R}(0)$ and wave function $\psi(\vb{r},0)$, it has a unique trajectory $t\mapsto \vb{R}(t)$. However, considering different experimental runs, the initial positions are random, with distribution given by $|\psi(\vb{r},0)|^2$---the quantum equilibrium distribution---(which implies that the position is distributed according to $|\psi(\vb{r},t)|^2$ at time $t$). As such, both the detection locations and times of a particle are random in different runs of a scattering experiment.

Bohmian trajectories for the DSE are shown in Fig. [\[fig:DSE_trajectories\]](#fig:DSE_trajectories){reference-type="ref" reference="fig:DSE_trajectories"}b, and are well-known; they feature invariably in expositions of Bohmian mechanics. DSE trajectories were first presented by Philippidis *et al.* in the late 1970s [@Dewdney] and have been reproduced various times using different methods [@BohmDS; @Sanz; @holland2; @gondran]. Most presentations make do with a freely propagating wave function, not employing a double-slit potential. Here, they are produced without this simplifying assumption. See also [@Kocsis] for a weak measurement of average trajectories in a DSE, which resemble those of Fig. [\[fig:DSE_trajectories\]](#fig:DSE_trajectories){reference-type="ref" reference="fig:DSE_trajectories"}b.

The trajectories provide an almost self-explanatory account of how the interference pattern builds up on a distant screen one particle at a time. In particular, they show "how the motion of a particle, passing through just one of two holes in \[a\] screen, could be influenced by waves propagating through both holes. And, so influenced that the particle does not go where the waves cancel out, but is attracted to where they cooperate" [@Bell p. 191]. It follows that interference experiments can be accounted for in terms of particle trajectories, claims to the contrary notwithstanding.[^1]

To produce the Bohmian trajectories in Fig. [\[fig:DSE_trajectories\]](#fig:DSE_trajectories){reference-type="ref" reference="fig:DSE_trajectories"}b, Schrödinger's equation was solved numerically with initial Gaussian wave function centered at $(-\kern 0.1emx_0,0,-\kern 0.1emz_0)$ in front of the slits: $$\label{eq:GGG}
    \psi(\vb{r},0)= \frac{e^{i(k_xx+k_zz)}}{\sqrt{\sigma_x\kern 0.1em\sigma_y\kern 0.1em\sigma_z}} G\!\left(\!\frac{x+x_0}{\sigma_x}\!\right)\kern-0.1em G\!\left(\!\frac{y}{\sigma_y}\!\right)\kern-0.1em G\!\left(\!\frac{z+z_0}{\sigma_z}\!\right)\!,$$ where $\smash{G(\xi)=\pi^{-1/4}\exp(-\,\xi^2/2)}$.

The screen containing the slits was modelled by the Gaussian potential barrier $$\begin{aligned}
\label{eq:pot}
    V = V_0\kern 0.1emG\!\left(\!\frac{z}{\sigma_b}\!\right)\!\left[1-f_1S\!\left(\!\frac{x-\Delta}{\sigma_s}\!\right)-f_2\kern 0.1emS\!\left(\!\frac{x+\Delta}{\sigma_s}\!\right)\right],
\end{aligned}$$ featuring two rectangular apertures for $\smash{f_1=f_2=1}$,[^2] as shown in Fig. [\[fig:DSE_trajectories\]](#fig:DSE_trajectories){reference-type="ref" reference="fig:DSE_trajectories"}a. Here, $\smash{S(\xi)=1\raisebox{-0.2ex}{\resizebox{!}{1.6ex}{\kern 0.1em/\kern 0.1em}}(1+\xi^{16})}$, $2\Delta$, $\sigma_s$, and $\sigma_b$ respectively denote the aperture function, inter-slit separation, slit width, and the thickness of the barrier. Throughout the present work, masses, lengths and times are expressed in units of $m$, $\Delta$ and $\smash{m\Delta^2\kern-0.1em\raisebox{-0.2ex}{\resizebox{!}{1.6ex}{\kern 0.1em/\kern 0.1em}}\hbar}$, respectively. (This is equivalent to setting $\smash{\hbar=m=\Delta=1}$.) The Bohmian trajectories were computed by numerically integrating the guidance equation [\[eq:guide\]](#eq:guide){reference-type="eqref" reference="eq:guide"} for $5\times 10^5$ initial positions randomly sampled from the $|\psi(\vb{r},0)|^2$-distribution. About 15% of the sampled trajectories made it through the slits giving rise to detection events. The rest (not shown in Fig. [\[fig:DSE_trajectories\]](#fig:DSE_trajectories){reference-type="ref" reference="fig:DSE_trajectories"}b) were back-scattered from the potential barrier.

[^1]: For instance, "it is clear that \[the DSE\] can in no way be reconciled with the idea that electrons move in paths. \... In quantum mechanics there is no such concept as the path of a particle." [@LandauLifshitz p. 2], or that "many ideas have been concocted to try to explain the curve for $P_{12}$ \[the interference pattern\] in terms of individual electrons going around in complicated ways through the holes. None of them has succeeded." [@Feynman Sec. 1.5].

[^2]: For the dynamic DSE problem considered below, $f_{1,2}$ are varied in time as per Eq. [\[eq:dynamicT\]](#eq:dynamicT){reference-type="eqref" reference="eq:dynamicT"}.
