---
doc_id: arxiv-astro-ph-0203462v1
doc_title: "arXiv:astro-ph/0203462v1 26 Mar 2002"
section_id: sec-007-42-error-budget
section_title: "Error budget"
section_number: 4.2
pages: 7-13
source_pdf: 0203462v1.pdf
source_sha256: 337c24b051365f0a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 0.995
---
\label{errors}

Table \ref{T-error} summarizes the various sources of uncertainties affecting
the derived neutron-capture-element abundances in \cs.  Stochastic errors
($\Delta$(obs) listed in column 6) arise from random uncertainties in
the oscillator strengths (gf values) and in the measured equivalent widths.
The magnitude of this error is estimated as $\sigma$/$\sqrt{N-1}$
(where $\sigma$ is the rms around the mean abundance) when N$\geq$2 lines of a
given element are observed, otherwise as the quadratic sum of the estimated
error on the adopted gf value and the fitting uncertainty. Systematic
uncertainties include those which exist in the adopted oscillator strengths,
in the equivalent width measurements, mostly related to continuum location, and
in the adopted stellar parameters. The first
is extremely difficult to assess and is not considered explicitly here,
although it might be significant 
(gf values from various sources may be cross-checked, but often 
only one source is available).  The second should be negligible,
given the very high quality of our data.  Hence we have examined here only
those errors linked to our choice of stellar parameters.  These were estimated
by varying T$_{eff}$ by +100K, $\log g$ by +0.3 dex, and $\xi$ by +0.2kms$^{-1}$
in the stellar atmosphere model (columns 2, 3, and 4, respectively).
The quantity $\Delta$(T,$\log g$,$\xi$) listed in column 5 is the total impact
of varying each of the three parameters, computed as the quadratic sum of
columns 2, 3, and 4. The total uncertainty $\Delta$(total) (column 7)
on the {\it absolute} abundance of each element ($\log \epsilon$(X))
is computed as the quadratic sum of the stochastic
and systematic errors.  Columns 8 and 9 list the total uncertainties
on the abundance ratios X/U and X/Th.  Note that, due to the similarity of the 
response of a given set of elements to changes in the stellar parameters, 
systematic errors largely cancel out in the measured {\it ratios} of these 
elements, reducing the uncertainty affecting the {\it relative}
abundances. However, for the few species that are determined from
neutral lines, the stellar parameters uncertainties impact on the
[X/Th] or [X/U] ratio is not negligible anymore (eg. Ru, Rh, Pd).

In the following discussion, since we are mostly concerned by the {\it
relative} abundance ratios, we chose to consider the total uncertainties on the
X/Th ratio as representative of the uncertainty on the abundance pattern (in
Figs. \ref{F-r-sun} and \ref{F-r-cs22}, and listed in column $\Delta \log
\epsilon$(X/Th) of table \ref{T-heavy}).

\begin{table*}
\begin{center}
\caption{Error budget for neutron-capture elements
\label{T-error} }
\begin{tabular}{lcccccccc}
\hline
El. & $\Delta$T &  $\Delta\log g$ &  $\Delta \xi$ & $\Delta$(T,$\log g$,$\xi$) 
& $\Delta$(obs) & $\Delta$(total) 
& $\Delta \log \epsilon$(X/U) & $\Delta \log \epsilon$(X/Th) \\
      & +100K & +0.3dex       & +0.2kms$^{-1}$ \\
(1) & (2) & (3) & (4) & (5) & (6) &(7) & (8) & (9) \\ 
\hline
Sr II & 0.064 & 0.045 & $-$0.047 & 0.092 & 0.030 & 0.10 & 0.13 &  0.08 \\ 
 Y II & 0.068 & 0.082 & $-$0.057 & 0.121 & 0.023 & 0.12 & 0.13 &  0.06 \\ 
Zr II & 0.066 & 0.087 & $-$0.034 & 0.114 & 0.075 & 0.14 & 0.14 &  0.09 \\ 
Nb II & 0.044 & 0.091 & $-$0.019 & 0.128 & 0.150 & 0.20 & 0.19 &  0.15 \\
Ru I  & 0.079 &$-$0.021 &$-$0.012 & 0.159 & 0.050 & 0.17 & 0.18 &  0.14 \\
Rh I  & 0.080 &$-$0.019 &$-$0.007 & 0.162 & 0.021 & 0.16 & 0.17 &  0.13 \\
Pd I  & 0.081 &$-$0.023 &$-$0.024 & 0.166 & 0.071 & 0.18 & 0.19 &  0.15 \\
Ag I  & 0.081 &$-$0.022 &$-$0.020 & 0.166 & 0.170& 0.24 & 0.24 &  0.22 \\
Ba II & 0.096 & 0.046 & $-$0.075 & 0.122 & 0.076 & 0.14 & 0.16 &  0.11 \\ 
La II & 0.080 & 0.083 & $-$0.056 & 0.128 & 0.020 & 0.13 & 0.12 &  0.06 \\ 
Ce II & 0.078 & 0.089 & $-$0.013 & 0.119 & 0.035 & 0.12 & 0.12 &  0.04 \\ 
Pr II & 0.078 & 0.089 & $-$0.012 & 0.119 & 0.054 & 0.13 & 0.12 &  0.06 \\ 
Nd II & 0.078 & 0.086 & $-$0.024 & 0.119 & 0.041 & 0.13 & 0.12 &  0.05 \\     
Sm II & 0.082 & 0.089 & $-$0.010 & 0.122 & 0.057 & 0.13 & 0.12 &  0.06 \\ 
Eu II & 0.078 & 0.090 & $-$0.014 & 0.120 & 0.039 & 0.13 & 0.12 &  0.05\\
Gd II & 0.074 & 0.088 & $-$0.032 & 0.120 & 0.053 & 0.13 & 0.13 &  0.06 \\ 
Tb II & 0.078 & 0.091 & $-$0.016 & 0.121 & 0.029 & 0.12 & 0.11 &  0.04 \\
Dy II & 0.076 & 0.088 & $-$0.023 & 0.118 & 0.058 & 0.13 & 0.13 &  0.07 \\     
Er II & 0.078 & 0.080 & $-$0.088 & 0.142 & 0.040 & 0.15 & 0.15 &  0.09 \\ 
Tm II & 0.092 & 0.053 & $-$0.043 & 0.115 & 0.058 & 0.13 & 0.14 &  0.08 \\ 
Hf II & 0.042 & 0.086 & $-$0.028 & 0.123 & 0.170 & 0.21 & 0.20 &  0.17 \\ 
Os I  & 0.078 & 0.011 & $-$0.008 & 0.157 & 0.120 & 0.20 & 0.19 &  0.16 \\ 
Ir I  & 0.065 & 0.045 & $-$0.024 & 0.140 & 0.090 & 0.17 & 0.15 &  0.11 \\ 
Th II & 0.048 & 0.090 & $-$0.008 & 0.132 & 0.020 & 0.13 & 0.11 & \dots \\ 
 U II & 0.046 & 0.093 & $-$0.002 & 0.131 & 0.110 & 0.17 & \dots &  0.11 \\ 
\hline\hline
\end{tabular}
\end{center}
\end{table*}


   \begin{figure*}
   \centering
   {\includegraphics[angle=0,height=7.1cm]{M2317f13.ps}
    \includegraphics[angle=0,height=7.1cm]{M2317f14.ps}
    \includegraphics[angle=0,width=7.7cm]{M2317f15.ps}}
      \caption{The observed Os~I 4261 \AA, 4420 \AA, and Ir~I 3513 \AA\ 
    lines in \cs. Symbols as in
      Fig. \ref{F-C}.}
         \label{F-Os-Ir}
   \end{figure*}

   \begin{figure}
   \centering
   {\includegraphics[angle=0,width=8cm]{M2317f16.ps}
   \includegraphics[angle=0,width=8cm]{M2317f17.ps}}
      \caption{The observed Pb I 4057 \AA\ lines in \cs 
      (upper panel) and \sned (lower panel). Symbols as in Fig. \ref{F-C}.} 
        \label{F-Pb}
   \end{figure}


\subsection{The lighter elements, 38$\leq$Z$\leq$48}

This group includes the classically observed elements Sr, Y, and Zr, but also
the less well-studied species Nb, Ru, Rh, Pd, and Ag, whose lines are weak and
lie in the near-UV part of the spectrum, hampering their detection in normal
metal-poor halo giants.  The only metal-poor star in which all 
these elements have been previously detected is \sned (Sneden et al.
\cite{sneden00}), thanks to its large enhancement of neutron-capture elements.
In \cs we detected even more lines of these elements (due to the slightly 
larger metallicity, reduced blending by CH, CN and NH molecules, and better spectrum quality); Figs. \ref{F-Nb-Ru-Rh}
and \ref{F-Pd-Ag} show
examples of the quality of the fits obtained. However, one element detection 
remains inconclusive -- even the strongest expected transition of Cd~I in
our wavelength domain (3261.05 \AA) is too severely blended to be useful for
abundance determinations.
 
In Solar System material, the four lighter elements are dominated by
products of the main s-process (with a possible contribution from the weak
s-process as well; see Prantzos et al. \cite{prantzos90}, Tsujimoto et al.
\cite{tsujimoto00}), while the elements Ru, Rh, Pd, and Ag may contain a large 
r-process fraction (54\% to 86\%). However, in a star as metal-poor as \cs,
it is expected that the s-process contribution should be negligible, both from
a theoretical point of view (the main s-process takes place in AGBs, where
the contribution depends on metallicity via the abundances of both seed
nuclei and neutron sources, e.g.  Prantzos et al. \cite{prantzos90}), and from
an observational point of view (Burris et al. \cite{burris00} and references
therein). Thus, all these elements should represent r-process material
produced in the early Galaxy.  

In Fig. \ref{F-r-sun} we compare the observed
abundance pattern in \cs to the Solar System r-process abundances, scaled to
the abundance of \cs (see section \ref{second-peak} for details of the scaling
procedure). These Solar System r-process abundances are obtained from a
de-composition of the Solar abundances (Anders \& Grevesse \cite{grevesse89})
into their s- and r-process fractions, by subtraction of computed main
s-process yields (AGB yields) from the total abundances to obtain the r-
process fraction. We show here two sources for this de-composition,
illustrating the uncertainties involved.  The dashed line in Fig.
\ref{F-r-sun} follows the compilation of Burris et al. (\cite{burris00}), which
uses yields from K\"appeler et al.  (\cite{kappeler89}) and Wisshak et al.
(\cite{wisshak96}), while the solid line uses yields of AGB models from
Arlandini et al.  (\cite{arlandini99}).

It is clear from inspection of Fig. \ref{F-r-sun} that, although one can
argue the case for general agreement in the region of the second r-process
peak, the abundances of \cs in the region 38$\leq$Z$\leq$48 are not all
compatible with the Solar System r-process pattern. This effect is best seen in
the middle and lower panels of Fig. \ref{F-r-sun}, where the abundance
difference $\log \epsilon_{*} - \log \epsilon_{rSS}$ between \cs and the Solar 
System (SS) $r$-process are displayed. When the Burris el al. (\cite{burris00})
de-composition is used, the difference appears as a stronger odd-even effect in
\cs, in addition to a lower mean abundance: $<\log \epsilon_{*} - \log
\epsilon_{rSS}>_{38\leq Z\leq 48}=-1.47$ (rms 0.33) for the lighter elements 
vs. $<\log \epsilon_{*} - \log \epsilon_{rSS}>_{56\leq Z\leq 69}=-1.25$ 
(rms 0.10) for the heavier group.  
If the Arlandini et al. (\cite{arlandini99}) de-composition is used,
the result is very similar for Ru, Rh, and Ag.  Note that in this
case, the Y abundance is no longer discrepant, while Nb is significantly
more abundant than the Solar r-value.  As a result, the mean offsets
between the lighter and second-peak elements over large intervals
in atomic number are in fact quite similar,  $<\log \epsilon_{*} - \log
\epsilon_{rSS}>_{38\leq Z\leq 48}=-1.38$ (rms 0.33) compared to $<\log
\epsilon_{*} - \log \epsilon_{rSS}>_{56\leq Z\leq 69}=-1.28$ (rms 0.08).

Independently of the decomposition used, the most
discrepant element is silver, for which the solar system r-process
scaled abundance exceeds the \cs observed value by 0.8 dex ! This low
abundance of Ag was also observed in \sned by Sneden et
al. (\cite{sneden00}), and the good agreement
between the \cs and \sned silver abundances can be seen 
in Fig. \ref{F-r-cs22}).
In contrast, the only other metal-poor stars (4 halo stars with
$-2.15\leq$[Fe/H]$\leq -1.3$ dex) in which it was observed so
far (Crawford et al. \cite{crawford98}) demonstrated a mild [Ag/Fe]
enhancement, in agreement with the mild enhancement of the second
r-process peak elements in these stars. This illustrates that not
everything is understood in the way the r-process builds up elements in
the wide atomic mass-range in which it is at work.


\subsection{The second-peak elements, 56$\leq$Z$\leq$72}\label{second-peak}

The group of elements between barium and hafnium is the best studied mass-range
of the neutron-capture elements, thanks to the relatively strong lines in the
visible region of elements such as Ba, Eu, and La. In \cs we were able to 
detect lines from {\it all} stable elements between Z=56 and Z=72. However,
three of them cannot be used for abundance determinations because of poorly
known atomic physics --  Ho and Lu have very strong hyperfine structure which
is not well quantified; and while three lines of Yb were detected, two
are severely blended (3289\AA and 3476\AA), and the strongest one
(3694\AA) yields a very large abundance ($\log\epsilon$(Yb)=0.18),
which we believe is due to the unaccounted hyperfine
structure, which acts to de-saturate this strong line (123 m\AA). 
We are thus left with accurate abundance determinations for 13
elements in the second peak of the r-process. 
Fig. \ref{F-HfEu} are example of the fit respectively of a Hf and
a Eu line. Not that the europium hyperfine structure used here is from
Kurucz (Kurucz \cite{kuruczcd}), although the oscillator strength was
taken from the more recent work of Lawler et
al. \cite{lawler01b}. The Eu isotope composition
adopted was 47.8$\%$ of $^{151}$Eu and 52.2$\%$ of 
$^{151}$Eu, as in the solar system, and in accordance to the new
measurement of Sneden et al. (\cite{snedenEu}) who measured this
isotopic ratio to be solar in the two metal-poor r-process rich stars
BD\,+17\,3248, \hd115 and \sned. The europium isotopic composition of \cs
will be investigated in a forthcoming paper, together with the rest of
our sample of extremely metal poor stars.

The abundances of the second peak elements are displayed in Fig.
\ref{F-r-sun}, and compared to the Solar System r-process, scaled by the mean
abundance difference with \cs: $<\log \epsilon_{*} - \log
\epsilon_{rSS}>_{56\leq Z\leq 69}$.  Both the Burris et al. (\cite{burris00})
and the Arlandini et al. (\cite{arlandini99}) de-compositions are very similar
in this mass range, and the mean underabundances computed for \cs are 
$<\log \epsilon_{*} - \log \epsilon_{rSS}>_{56\leq Z\leq 69}=-1.25$ (rms 0.10) 
and $-1.28$ (rms 0.08), respectively.
The remarkable agreement of the abundance ratios in halo stars with the Solar
r-process pattern in this atomic mass-range has been noted already in several
papers (Sneden et al. \cite{sneden96},\cite{sneden00}; Westin et al.
\cite{westin00}; Johnson \& Bolte \cite{johnson01}), and is also seen
in giants of the globular cluster M15 (Sneden et al. \cite{snedenM15}). In this
respect \cs resembles other metal-poor stars, both mildly r-process-enhanced
(\hd115 and others, see Johnson \& Bolte \cite{johnson01}), and the extreme
r-process-enriched star \sned.  In fact, Fig. \ref{F-r-cs22} shows that the
neutron-capture-element pattern in \cs (this paper) and \sned\, (Sneden et
al. \cite{sneden00}) are virtually indistinguishable (\sned\, abundances have
been scaled by the mean difference between the two stars $<\log \epsilon_{\cs}
- \log \epsilon_{\sned}>_{56\leq Z\leq 69}=+0.17$ (rms 0.10)).  Note  that
while the absolute r-process abundances are larger in \cs, given the
metallicity difference between the two stars ([Fe/H]$_{\cs}=-2.9$ and
[Fe/H]$_{\sned}=-3.2$), the total [r/Fe] ratio in \cs\, in the mass range
56$\leq$Z$\leq$69 is 0.13 dex lower than in \sned.
     

\subsection{The third-peak elements and the actinides, 
76$\leq$Z$\leq$92}\label{actinides}

The third r-process peak (near the magic number N=126) is sampled in
\cs by Os and Ir. The two heaviest species detected are the radioactive
actinides Th and U, the use of which as chronometers we discuss in 
section \ref{age}.

   \begin{figure}
   \centering
   {\includegraphics[angle=0,width=4.2cm]{M2317f18.ps}
   \includegraphics[angle=0,width=4.2cm]{M2317f19.ps}
   \includegraphics[angle=0,width=4.2cm]{M2317f20.ps}
   \includegraphics[angle=0,,width=4.2cm]{M2317f21.ps}}
      \caption{The observed Th II 3351 \AA, 3434\AA, 4019\AA\, and 4086\AA\  
      lines in \cs. {\it Dots:} observations; {\it line:} synthetic spectrum
      computed for the mean Th abundance, $\log \epsilon$(Th)=-0.98.}
         \label{F-Th}
   \end{figure}

   \begin{figure*}
   \centering
   {\includegraphics[angle=0,height=7.5cm]{M2317f22.ps}
    \includegraphics[angle=0,height=7.5cm]{M2317f23.ps}}
    \caption{The observed U~II 3859 \AA\ line in \cs. Symbols as in Fig.
      \ref{F-C}. The best fit is found for $\log \epsilon$(U)=$-$1.92 
      (thick line).}
         \label{F-U}
   \end{figure*}


\noindent{\it Osmium and Iridium}\\
Fig. \ref{F-Os-Ir} shows two of the three osmium detections, and one of the
two iridium detections. It was suggested in our preliminary results (Hill et
al. \cite{hill01}) that these two elements were overabundant with respect to
the Solar r-process by around +0.3 dex.  We now revise this statement slightly.
In particular, Ir falls back to the same abundance scale as the $56\leq
Z\leq 69$ elements. The reason for this revision is connected with the code
used to derive abundances. In our preliminary analysis (Hill et al.
\cite{hill01}) we were using the code of Spite (\cite{codespite}), 
while
in the present analysis we have switched to a more self-consistent approach,
the synthesis code by Plez et al. (\cite{codeplez}), which employs the same
algorithms to compute the model atmosphere and the synthetic spectrum. The
main difference between the two codes lies in the continuous opacity
computations and the source function assumptions (a diffusive term is added in
the latter). These codes provide identical results above 4000 \AA\ (less
than 0.02 dex difference), but the present, presumably more reliable  
approach, yields systematically lower
abundances in the bluest part of the spectrum (with a maximum effect of
$\sim$0.2 dex).  In the case of Ir, the two lines at 3512 \AA\ and 3800 \AA\
gave discrepant results in our preliminary analysis, but now agree, with $\log
\epsilon(Ir)=0.2$ dex (instead of the earlier 0.37 dex which came from
the 3512 \AA\ line alone).

Osmium, on the other hand, still seems to be overabundant with respect
to both the scaled Solar r-process fraction and to \sned. If Os in \cs\, 
was enhanced
to the same level as the second r-process peak elements, we would expect
$\log \epsilon$(Os)=0.15 dex, and $\log \epsilon$(Os)=0.12 dex if it was
enhanced similarly to \sned, whereas we observe $\log
\epsilon$(Os)=0.43 dex (rms 0.17, from 3 lines). 
We investigated the
possible source of differences between our analysis and that of
Sneden et al. (\cite{sneden96}, \cite{sneden00}), which could explain
this difference: (i) The three lines used
here are the same as those used by Sneden et al. (same wavelengths, same excitation potential and same oscillator strengths), 
(ii) the ionisation potential of Os I adopted
here is from a measurement by  Colarusso et al. (\cite{colarusso97})
of 8.44eV, compared to 8.35eV adopted by Sneden et al. (\cite{sneden96}),
which could account for at most $\sim$0.1 dex difference in the final
abundance but in the wrong direction, (iii) the difference in the codes
used for the abundance determination cannot play a role {\it only for
osmium}, leaving all the other abundance determinations unaffected. 
Hence, at this point, we cannot account for the abundance discrepancy
by any obvious differences in the analysis. We are therefore left with the
possibility that the Os content of \cs is indeed larger than predicted
by a scaled Solar r-process. On  the other hand, the large abundance
dispersion observed from the three lines (rms 0.17) is a hint that
there may be hidden problems in the determination of Os abundance from
these lines, so that any strong conclusion would be premature at this stage.

\noindent{\it Lead}\\
Recently, accurate abundances of lead in metal-poor CH stars (the Pb having 
likely been transferred from a now-extinct AGB companion) were reported
by Aoki et al. (\cite{aoki00}) and Van Eck et al.  (\cite{vaneck01}), using the
4057.8 \AA\ line.  In \cs, this line is not visible. Hence, we can only assign 
an upper limit of $\log \epsilon$(Pb)$<-0.2$ dex ($\log \epsilon$(Pb)$=
-0.4^{+0.2}_{-\infty}$), as shown in Fig. \ref{F-Pb}. However, even this upper
limit is of great interest, since it is already {\it below} the expected
abundance of the scaled Solar System r-process fraction (Fig. \ref{F-r-sun}).

Noting from Fig. \ref{F-r-cs22} that our derived abundance of Pb is drastically
lower than the detection reported by Sneden et al. (\cite{sneden00})
for \sned,  
we re-assessed also the abundance of Pb in \sned from spectra taken
with VLT+UVES during the commissioning of the instrument
(http://www.eso.org/science/uves\_comm/). The spectrum was acquired
with a resolution of R=55,000; the S/N of the co-added spectrum 
(total exposure time of 4.5h) is $\sim$140 per (0.013\AA) pixel at 4100\AA\ 
(i.e., S/N$\sim$330 per resolution element).
The model for \sned is an OSMARCS
model with $T_{eff}=$4700K, $\log g=$1.5, [Fe/H]=-3.0 and [$\alpha$/Fe]=+0.40
(following Sneden et al. \cite{sneden00}).  The syntheses were generated with
$\xi$=2.1 kms$_{-1}$, [Fe/H] = $-$3.2, 
and individual abundances from Sneden et al.
(\cite{sneden96}). C and N abundances were determined, through a fit of the
3850-3900 \AA\ region (CH and CN bandheads), to be  $\log
\epsilon$(C)=6.07 ([C/Fe]=+0.75) and $\log \epsilon$(N)=5.42 ([N/Fe]=+0.70).
Then the Pb region was synthesized (some gf values of nearby atomic lines were
adjusted to fit the observed spectrum).  The Pb line lies in the red wing of a 
CH line, which is nicely fitted with the abundances derived from the
3850--3900 \AA\ region. Spectra were computed for $\log
\epsilon$(Pb)=$-$0.5, 0.0, 0.5,  
and no Pb. From inspection of Fig. \ref{F-Pb} we derive an upper limit for 
the Pb abundance of
$\log \epsilon$(Pb)$< 0.0$ ($\log \epsilon$(Pb)$= -0.25^{+0.25}_{-\infty}$).
The Pb contents of \sned\, and \cs, therefore, do not seem to be very
different,  and the reality of the measurement by Sneden et
al. (\cite{sneden00}) appears open to question.

\noindent{\it Thorium and Uranium}\\
The oscillator strengths of the single U~II line and eight of the Th~II lines
that we have measured in \cs (Table \ref{T-Th}), as well as many others, have
been re-determined with superior accuracy by Nilsson et al. (\cite{nilsson01a},
\cite{nilsson01b}). The associated change in the U/Th abundance ratio is quite
significant, as the oscillator strengths of the Th~II lines decrease by 0.07
dex, on average, whereas the $\log gf$ of the U~II line increases from $-$0.20
to $-$0.067, i.e., by 0.13 dex.  Moreover, the uncertainties associated with
the oscillator strengths have been reduced drastically (to better than 0.08
dex for the individual Th lines, and to only 0.06 dex for the U~II line), thus
they are a negligible source of error compared to the uncertainties in the
actual fit of the data.  Fig. \ref{F-Th} displays the synthesis of a
selection of the observed thorium lines, all plotted with a thorium abundance
equal to the mean of the eight lines ($\log \epsilon$(Th)=$-0.98$). 
The observed
uncertainty in this case was estimated as $\sigma/\sqrt{N-1}$, where $\sigma$
is the dispersion around the mean and N, the number of lines, hence leading to
a $\log \epsilon(Th)=-0.98\pm 0.02$.  

Fig. \ref{F-U} shows the region of the
U~II 3859 \AA\ line and an enlargement of the uranium line itself, together
with synthetic spectra for four different uranium abundances.  The accuracy of 
the fit is estimated to be around 0.1 dex, obtained by testing the influence 
of several potential sources of error on the fitting procedure, including 
placement of the continuum and blending by neighboring lines (mainly Fe~I
3859.9 \AA). The uncertainty arising from the blending of
the Fe~I line is linked to uncertainties on the oscillator strength,
but also the broadening factor of the line. The Van der waals
broadening factor was taken from Barklem et al. \cite{barklem2}, and the
oscillator strength was increased by 0.1 dex with respect to the VALD2
recommended value to give
a best fit to the observed line Fe~I 3859.9~\AA. 
Attempts to vary the Barkelem damping constant by 5\% or more induced
changes in the U abundance of less than 10\%. The unidentified 
features on the red side of the line (at 3860.77 and 3860.9~\AA\
respectively) hamper the cosmetics of the fit but have no influence on the uranium line region. We would like to
point out that the 3860.77~\AA\ unidentified line also appears in the
spectrum of \sned, whereas
it does not in other giants of similar metallicity and temperature
which have no excess of neutron-capture elements. We
therefore tentatively attribute this absorption feature to an
neutron-capture element, and encourage atomic physicists to work on
the identification of this feature. We also note here that there are
numerous features in the whole UV part of the spectrum of
neutron-capture enriched giants, that are still in need of identification.
A more detailed analysis of the 5-line feature (Fe~I 3859.21, 
Nd~II 3859.4, U~II 3859.57, CN 3859.67 and Fe~I 3859.9~\AA) 
is forseen is a near future, involving 3D hydrodynamical models.
Adding the 0.06 dex uncertainty associated with the $\log gf$ of
the line results in $\log \epsilon(U)=-1.92\pm 0.11$. 
As seen from Table \ref{T-error}, the overall uncertainty of the U/Th ratio is 
totally dominated by that of the U line fitting procedure, while errors in the 
stellar parameters cancel out completely.

Finally, we note that, using the newly determined oscillator strength value for 
the uranium line, the upper limit deduced by Gustafsson \& Mitzuno-Wiedner
(\cite{gustafsson01}) for \sned\, becomes $\log \epsilon$(U)$\leq -2.54$.
