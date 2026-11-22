---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-021-26-time-step-error-structure
section_title: "Time Step Error Structure"
section_number: 2.6
pages: 45-47
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.902
latex_coverage_ratio: 0.985
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 73 sections: Front matter; ABSTRACT; ACKNOWLEDGEMENTS"
---
[]{#secErrEst label="secErrEst"} For the AV6' interaction, there are only the first 6 operators in Eq.([\[AV6\'\]](#AV6'){reference-type="ref" reference="AV6'"}), so $\mathcal{G}$ is 1, and Eq.([\[propagatorN2LOVTV\]](#propagatorN2LOVTV){reference-type="ref" reference="propagatorN2LOVTV"}) becomes the high-accuracy Trotter formula[^1] ([@Feynman1948RMP; @SchmidtLee95a]) which has $\mathcal{O}(\Delta \tau)^3$ accuracy and can be denoted as $U_S(\Delta \tau)$, $$U_S(\Delta \tau) \equiv
e^{-\frac{\mathcal{V}^\dagger}{2} \Delta \tau }
e^{-T \Delta \tau} e^{-\frac{\mathcal{V}}{2} \Delta \tau }
= e^{- H \Delta \tau
- \frac{ {\Delta \tau}^3}{24}[2T+\mathcal{V}, [T,\mathcal{V}]] + ... }
= e^{- H \Delta \tau} + \mathcal{O}(\Delta \tau)^3,
\label{HighTrotter}$$ where the subscript letter $S$ means symmetric because $U_S(\Delta \tau)=U^\dagger_S(\Delta \tau)$. Note that although the approximation of $e^{-\frac{\mathcal{V}}{2} \Delta \tau }$ which is Eq.([\[propagatorv6half\]](#propagatorv6half){reference-type="ref" reference="propagatorv6half"}) alone has $\mathcal{O}(\Delta \tau^2)$ error, when written the form of Eq.([\[HighTrotter\]](#HighTrotter){reference-type="ref" reference="HighTrotter"}), the $\mathcal{O}(\Delta \tau^2)$ cancels and one is left with only $\mathcal{O}(\Delta \tau^3)$ error. Furthermore, we find $$U_S(\Delta \tau) U_S(-\Delta \tau)=1,
\label{USuni}$$ this ensures the error in the exponential of $U_S(\Delta \tau)$ only contains odd orders of $\Delta \tau$, $$U_S(\Delta \tau) = e^{-H \Delta \tau
+ \hat{f}_3 \Delta \tau^3
+ \hat{f}_5 \Delta \tau^5
+ \hat{f}_7 \Delta \tau^7 + ... } ,
\label{propagatorerrstruc}$$ where $\hat{f}_i$ are functions of operators which do not depend on $\Delta \tau$.

For the AV6' interaction, in the PIMC calculation, we use $N$ short-time propagator $[U_S(\Delta \tau)]^N$ instead of $(e^{-H \Delta \tau})^N$ in calculating Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}), and the total imaginary time $\tau=N\Delta \tau$, so $N\mathcal{O}(\Delta \tau^n)=\tau \mathcal{O}(\Delta \tau^{n-1})$. Considering Eq.([\[propagatorerrstruc\]](#propagatorerrstruc){reference-type="ref" reference="propagatorerrstruc"}), this means that for a given $\tau$, the error of $[U_S(\Delta \tau)]^N$ only contain the even orders of $\Delta \tau$, $$\left[U_S(\Delta \tau)\right]^N =
\left(e^{ -H \Delta \tau
+ \hat{f}_3 \Delta \tau^3
+ \hat{f}_5 \Delta \tau^5 + ... }\right)^N
=e^{-H \tau} + \mathcal{O}(\Delta \tau^2) + \mathcal{O}(\Delta \tau^4) + ... ,
\label{propagatorNerrstruc}$$ and this means $\langle \hat{O} (\Delta \tau) \rangle$ in Eq.([\[PIMCopexpdetailshorttimeapprox\]](#PIMCopexpdetailshorttimeapprox){reference-type="ref" reference="PIMCopexpdetailshorttimeapprox"}) and the true expectation value $\langle \hat{O} \rangle$ of Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}) are related by the following equation, $$\begin{aligned}
\langle \hat{O} (\Delta \tau) \rangle
& = \frac{ Re  \langle \Psi_T| [U_S(\Delta \tau)]^{N_1} \hat{O} [U_S(\Delta \tau)]^{N_2}| \Psi_T \rangle  }
{ Re \langle \Psi_T| [U_S(\Delta \tau)]^{N} | \Psi_T \rangle} \nonumber \\
& = \langle \hat{O} \rangle \times
\frac{1 + \mathcal{O}(\Delta \tau^2) + \mathcal{O}(\Delta \tau^4) + ... }
{1+ \mathcal{O}(\Delta \tau^2) + \mathcal{O}(\Delta \tau^4) + ... } .
\label{PIMCUSdetail}
\end{aligned}$$ For small $\Delta\tau$, in order to extrapolate the expectation value $\langle \hat{O} \rangle$, we need to use, $$\langle \hat{O} (\Delta \tau) \rangle
= \langle \hat{O} \rangle
+ \sum_{n=1}^{n_c} C_{2n} (\Delta \tau^{2n}),
\label{Oextrapolation}$$ where $C_{2n}$ are the fitting parameters for even orders of $\Delta \tau$, and $n_c$ is the cutoff integer for $n$. The theoretical value of $C_{2n}$ depends on the trial wave function and the total imaginary time $\tau$. In principle, a general extrapolation formula which suits a wide range of $\Delta \tau$ should have the same form as Eq.([\[PIMCUSdetail\]](#PIMCUSdetail){reference-type="ref" reference="PIMCUSdetail"}).

For the local chiral N$^2$LO interaction, we use the $U(\Delta \tau)$ in Eq.([\[propagatorN2LOVTV\]](#propagatorN2LOVTV){reference-type="ref" reference="propagatorN2LOVTV"}) as the short-time propagator and it has errors $\mathcal{O}(\Delta \tau^2)$, so when the total imaginary time $\tau=N\Delta \tau$, we multiply $U(\Delta \tau)$ the short-time propagator $N$ times we have error of $N\mathcal{O}(\Delta \tau^2)=\tau \mathcal{O}(\Delta \tau)$ which is $\mathcal{O}(\Delta \tau)$, $$\left[U(\Delta \tau)\right]^N = e^{-H \tau} + \mathcal{O}(\Delta \tau),
\label{propagatorNerrstruc}$$ this means that the error of $\langle \hat{O} (\Delta \tau) \rangle$ in Eq.([\[PIMCopexpdetailshorttimeapprox\]](#PIMCopexpdetailshorttimeapprox){reference-type="ref" reference="PIMCopexpdetailshorttimeapprox"}) has $\mathcal{O}(\Delta \tau)$ error, $$\begin{aligned}
\langle \hat{O} (\Delta \tau) \rangle
& = \frac{ Re  \langle \Psi_T| [U(\Delta \tau)]^{N_1} \hat{O} [U(\Delta \tau)]^{N_2}| \Psi_T \rangle  }
{ Re \langle \Psi_T| [U(\Delta \tau)]^N | \Psi_T \rangle} \nonumber \\
& = \langle \hat{O} \rangle \times
\frac{1 + \mathcal{O}(\Delta \tau) + \mathcal{O}(\Delta \tau^2) + \mathcal{O}(\Delta \tau^3) + ... }
{1+ \mathcal{O}(\Delta \tau) + \mathcal{O}(\Delta \tau^2) + \mathcal{O}(\Delta \tau^3) + ... } .
\label{PIMCUN2LOdetail}
\end{aligned}$$ Similar with the Taylor expansion of $\frac{1}{1+x}=1-x+...$ requires $|x|<1$ to converge, when the error in the denominator in Eq.([\[PIMCUN2LOdetail\]](#PIMCUN2LOdetail){reference-type="ref" reference="PIMCUN2LOdetail"}) is less than one, Eq.([\[PIMCUN2LOdetail\]](#PIMCUN2LOdetail){reference-type="ref" reference="PIMCUN2LOdetail"}) can be written as, $$\begin{aligned}
\langle \hat{O} (\Delta \tau) \rangle
= \langle \hat{O} \rangle
+ \mathcal{O}(\Delta \tau) + \mathcal{O}(\Delta \tau^2) + ... .
\end{aligned}$$ So, usually, for a given total time $\tau$ and small $\Delta \tau$, in order to get the true expectation value $\langle \hat{O} \rangle$ of Eq.([\[PIMCopexpdetailshorttime\]](#PIMCopexpdetailshorttime){reference-type="ref" reference="PIMCopexpdetailshorttime"}), we need to calculate $\langle \hat{O} (\Delta \tau) \rangle$ for difference time step $\Delta \tau$ and error bar, and then use the following polynomial equation to extrapolate $\langle \hat{O} \rangle$ and its error bar, $$\langle \hat{O} (\Delta \tau) \rangle
= \langle \hat{O} \rangle
+ \sum_{n=1}^{n_c} C_{n} (\Delta \tau^{n}),
\label{ON2LOextrapolation}$$ where $C_n$ are fitting parameters and the theoretical value of $C_{n}$ depends on the trial wave function and the total imaginary time $\tau$. In principle a general extrapolation expression should be Eq.([\[PIMCUN2LOdetail\]](#PIMCUN2LOdetail){reference-type="ref" reference="PIMCUN2LOdetail"}).

From the error structure Eq.([\[PIMCUSdetail\]](#PIMCUSdetail){reference-type="ref" reference="PIMCUSdetail"}) or Eq.([\[PIMCUN2LOdetail\]](#PIMCUN2LOdetail){reference-type="ref" reference="PIMCUN2LOdetail"}) we can see that, even if $\Delta \tau$ itself is not very small, as long as the $\Delta \tau$ errors (especially the leading order errors) in the numerator and the denominator of Eq.([\[PIMCUSdetail\]](#PIMCUSdetail){reference-type="ref" reference="PIMCUSdetail"}) or Eq.([\[PIMCUN2LOdetail\]](#PIMCUN2LOdetail){reference-type="ref" reference="PIMCUN2LOdetail"}) are comparable, $\langle \hat{O} (\Delta \tau) \rangle$ can still be close to the true expectation value $\langle \hat{O} \rangle$. That is to say the results of PIMC is robust because they may not be very sensitive to the time step $\Delta \tau$.

[^1]: All the error structures of the propagator can be found by repeatedly using Campbell-Baker-Hausdorff (CBH) formula ([@Reinsch2000JMP]), $$\begin{aligned}
    e^A e^B = e^{A+B+\frac{1}{2}[A,B]+\frac{1}{12}[A-B,[A,B]]+\frac{1}{24}[B,[A,[B,A]]] + ...},
    \label{CBHformula}
     
    \end{aligned}$$ where A and B are operators or matrices. From Eq.([\[CBHformula\]](#CBHformula){reference-type="ref" reference="CBHformula"}) we can further find that, $$e^{\frac{B}{2} }  e^{A}  e^{\frac{B}{2}}
    = e^{A+B
    + \frac{1}{24}[2A+B, [A,B]] + ... }.$$ and that is how we can write down ([@VesaPDF]) Eq.([\[HighTrotter\]](#HighTrotter){reference-type="ref" reference="HighTrotter"}).
