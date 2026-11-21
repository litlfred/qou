---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-031-321-single-bead-sampling
section_title: "Single-Bead Sampling"
section_number: 3.2.1
pages: 66-69
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.885
latex_coverage_ratio: 1.0
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#Sample1bead label="Sample1bead"}

From $\mathcal{R}=\{ R_0, ..., R_K, ..., R_N \}$, we can propose to move just one bead, bead $K$, we move $R_K$ to $R_K'$, then $\mathcal{R}'=\{ R_0, ..., R_K', ..., R_N \}$. This is single bead sampling.

For the $K = 0$ or $N$ case, the $g^F(\mathcal{R}')$ in Eq.([\[gF\]](#gF){reference-type="ref" reference="gF"}) becomes, $$\begin{aligned}
g^F(\mathcal{R}')|_{R_0 \rightarrow R_0'} &= G^f_{0', 1} \prod_{I=1}^{N-1} G^f_{I, I+1} , \label{gFRnew1bead0} \\
g^F(\mathcal{R}')|_{R_N \rightarrow R_N'} &= G^f_{N-1, N'} \prod_{I=0}^{N-2} G^f_{I, I+1} , \label{gFRnew1beadN}
\end{aligned}$$ where $G^f_{0' 1 }$ and $G^f_{N-1, N'}$ are as defined in Eq.([\[Gfii1\]](#Gfii1){reference-type="ref" reference="Gfii1"}) and can be calculated by Eq.([\[propagatorFree\]](#propagatorFree){reference-type="ref" reference="propagatorFree"}), $$\begin{aligned}
G^f_{0', 1}  &=  \langle R'_{0} | e^{-T \Delta \tau}  | R_{1} \rangle =  \left( \frac{m}{2\pi \Delta \tau \hbar^2} \right)^{\frac{3A}{2}}
 e^{  -\frac{ ({R'_{0}}-{R_1})^2 }{2 \Delta \tau  \frac{\hbar^2}{m}  }}   ,
\label{gFRnew1bead0a} \\
G^f_{N-1, N'}  &=  \langle R_{N-1} | e^{-T \Delta \tau}  | R'_{N} \rangle
=  \left( \frac{m}{2\pi \Delta \tau \hbar^2} \right)^{\frac{3A}{2}}
 e^{  -\frac{ (R_{N-1}-R'_{N})^2 }{2 \Delta \tau \frac{\hbar^2}{m} }  }  .
\label{gFRnew1beadKa}
\end{aligned}$$

We can just set the proposed transition probability as, $$\begin{aligned}
T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') |_{R_0 \rightarrow R_0'} &=
G^f_{0', 1},
 \label{Tlrnew0} \\
T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') |_{R_N \rightarrow R_N'} &=
G^f_{N-1, N'},
 \label{TlrnewN}
\end{aligned}$$ and then Eq.([\[Acc2\]](#Acc2){reference-type="ref" reference="Acc2"}) becomes Eq.([\[acc2simp\]](#acc2simp){reference-type="ref" reference="acc2simp"}) and we use Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}) to judge if we accept $R_K'$ and thus $\mathcal{R}'$ or not.

For the $K \neq 0$ or $N$ case, the corresponding $g^F(\mathcal{R}')$ becomes, $$g^F(\mathcal{R}') = G^f_{K-1, K'} G^f_{K', K+1} \prod_{I=0}^{K-2} G^f_{I, I+1} \prod_{I=K+2}^{N-1} G^f_{I, I+1},
\label{gFRnew1bead}$$ where $G^f_{K-1, K'}$ and $G^f_{K', K+1}$ are the free propagators calculated by Eq.([\[Gfii1\]](#Gfii1){reference-type="ref" reference="Gfii1"}) or Eq.([\[propagatorFree\]](#propagatorFree){reference-type="ref" reference="propagatorFree"}).

In order to proceed, we introduce a useful relation in our calculation. For any coefficients $a$ and $b$ and any configuration $R_M$, $R_N$ and $R_L$, $$\begin{aligned}
\!\! \!\! \! a(R_M-R_N)^2\!+\!b(R_N-R_L)^2
\! = \! (a+b)
\!  \left(  R_N \!-\! \frac{aR_M\!+\!bR_L}{a\!+\!b} \right)^2
\!\! \! + \! \frac{ab}{a\!+\!b} \! \left( R_M \!-\! R_L  \right)^2, \label{Rdiffadd}
\end{aligned}$$ where each square can be calculated by using Eq.([\[Rdiffdef\]](#Rdiffdef){reference-type="ref" reference="Rdiffdef"}). In particular, if $a=b=1$, Eq.([\[Rdiffadd\]](#Rdiffadd){reference-type="ref" reference="Rdiffadd"}) just becomes, $$\begin{aligned}
(R_M-R_N)^2+(R_N-R_L)^2
= 2\left(  R_N -\frac{R_M+R_L}{2} \right)^2
+ \frac{\left( R_M-R_L  \right)^2}{2} . \label{Rdiffadd1}
\end{aligned}$$

By using Eq.([\[Rdiffadd1\]](#Rdiffadd1){reference-type="ref" reference="Rdiffadd1"}), the product of the two free particle propagators $G^f_{K-1, K'} G^f_{K', K+1}$ in Eq.([\[gFRnew1bead\]](#gFRnew1bead){reference-type="ref" reference="gFRnew1bead"}) becomes, $$G^f_{K-1, K'} G^f_{K', K+1}  =
\left( \frac{m}{2\pi \Delta \tau \hbar^2} \right)^{3A}
 e^{ -\frac{ \left({R_{K}'}-\frac{R_{K\!-\!1}+R_{K\!+\!1}}{2} \right)^2 }{ \Delta \tau  \frac{\hbar^2}{m}  } }
e^{ - \frac{ \left({R_{K\!-\!1}}-{R_{K\!+\!1}}\right)^2 }{ 4 \Delta \tau  \frac{\hbar^2}{m}  } } .

 \label{GKm1KpKpkp1}$$

We set the proposed transition probability $T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}')$ from Eq.([\[GKm1KpKpkp1\]](#GKm1KpKpkp1){reference-type="ref" reference="GKm1KpKpkp1"}) as, $$T_{l'r'}(\mathcal{R} \rightarrow \mathcal{R}') =
\left( \frac{m}{\pi \Delta \tau \hbar^2} \right)^{\frac{3A}{2}}
 e^{  -\frac{ \left({R_{K}'}-\frac{R_{K\!-\!1}+R_{K\!+\!1}}{2} \right)^2 }{ \Delta \tau  \frac{\hbar^2}{m}  }} .
 \label{Tlrnew}$$ The corresponding reverse transition probability $T_{lr}(\mathcal{R}' \rightarrow \mathcal{R})$ can be written as, $$T_{lr}(\mathcal{R}' \rightarrow \mathcal{R}) =
\left( \frac{m}{\pi \Delta \tau \hbar^2} \right)^{\frac{3A}{2}}
 e^{  -\frac{ \left({R_{K}}-\frac{R_{K\!-\!1}+R_{K\!+\!1}}{2} \right)^2 }{ \Delta \tau  \frac{\hbar^2}{m}  }} .
 \label{Tlrold}$$

Now we can see that $g^F(\mathcal{R}')  T_{lr}(\mathcal{R}' \! \rightarrow \! \mathcal{R}) = g^F(\mathcal{R}) T_{l'r'}(\mathcal{R} \! \rightarrow \! \mathcal{R}')$, so Eq.([\[Acc2\]](#Acc2){reference-type="ref" reference="Acc2"}) becomes Eq.([\[acc2simp\]](#acc2simp){reference-type="ref" reference="acc2simp"}) and we use Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}) to judge if we accept $R_K'$ and thus $\mathcal{R}'$ or not.

For particle i at bead $K$, we define its spatial coordinates as $\bm{r}^K_i \equiv (x^K_i,y^K_i,z^K_i)$, and its new proposed coordinates as $\bm{r'}^K_i \equiv ({x'}^K_i,{y'}^K_i,{z'}^K_i)$. So for the A-nucleon nuclei, $R_K=(\bm{r}^K_1, \bm{r}^K_2, ..., \bm{r}^K_A)$ and $R_K'=(\bm{r'}^K_1, \bm{r'}^K_2, ..., \bm{r'}^K_A)$. We also define a 3 dimensional vector $\bm{g}_i$ for particle $i$, $$\bm{g}_i=(g_{ix},g_{iy},g_{iz}), \label{gaussgi}$$ where $g_{ix},g_{iy},g_{iz}$ are all independent gaussian random numbers with average value 0 and variance 1.

The basic procedures of the algorithm is described as follows.

Step 1

:   Randomly pick an integer $K$ from 0 to $N$.

Step 2

:   For particle $i$ at bead $K$,

    1.  if $K=0$, according to Eq.([\[Tlrnew0\]](#Tlrnew0){reference-type="ref" reference="Tlrnew0"}), propose its new coordinates ${\bm{r}'}^0_i$ according to ${\bm{r}}^{1}_i$ at bead $1$, $${\bm{r}'}^0_i = \bm{r}^{1}_i + \bm{g}_i \sqrt{  \Delta \tau  \frac{\hbar^2}{m} } ,$$

    2.  If $K=N$, according to Eq.([\[TlrnewN\]](#TlrnewN){reference-type="ref" reference="TlrnewN"}), propose its new coordinates ${\bm{r}'}^N_i$ according to ${\bm{r}}^{N-1}_i$ at bead $N-1$, $${\bm{r}'}^N_i = \bm{r}^{N-1}_i + \bm{g}_i \sqrt{  \Delta \tau  \frac{\hbar^2}{m} } ,$$

    3.  If $K\neq 0,N$, according to Eq.([\[Tlrnew\]](#Tlrnew){reference-type="ref" reference="Tlrnew"}), propose its new coordinates ${\bm{r}'}^K_i$ according to ${\bm{r}}^{K-1}_i$ at bead $K-1$ and ${\bm{r}}^{K+1}_i$ at bead $K+1$, $${\bm{r}'}^K_i = \frac{\bm{r}^{K-1}_i+\bm{r}^{K+1}_i}{2} + \bm{g}_i \sqrt{ \Delta \tau  \frac{\hbar^2}{2 m} } ,$$

Step 3

:   Loop over step 2 for all the particles, $i$ from 1 to A. Then we have the new configuration $R_K'$.

Step 4

:   Use Eq.([\[Accptequationsimp\]](#Accptequationsimp){reference-type="ref" reference="Accptequationsimp"}) to judge if we accept the proposed configurations $\mathcal{R}'$ or not. Then go to step 1 and continue.

In the program, we store all the probability amplitudes $\phi^r_{M}(\mathcal{R},S)$ in Eq.([\[phirMR\]](#phirMR){reference-type="ref" reference="phirMR"}) and $\phi^l_{M}(\mathcal{R},S)$ in Eq.([\[philMR\]](#philMR){reference-type="ref" reference="philMR"}) for $M$ from 0 to $N$. Once any $R'_K$ is accepted, we need to update all the $\phi^r_{M}(\mathcal{R}',S)$ for $K \leq M \leq N$ and $\phi^l_{M}(\mathcal{R}',S)$ for $0\leq M \leq K$. This means we need to do about $N$ updates for just one accepted $R'_K$ (which is not economical), and therefore totally about $N^2$ updates for all the beads if they are accepted. Besides, single bead sampling usually has a very high acceptance rate, this indicates that the beads may not be moved far enough in the configuration space. Therefore it should not be used often in the program. It is however simple, and can be used as a check for more complicated algorithms.
