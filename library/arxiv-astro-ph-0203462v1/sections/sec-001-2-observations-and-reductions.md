---
doc_id: arxiv-astro-ph-0203462v1
doc_title: "arXiv:astro-ph/0203462v1 26 Mar 2002"
section_id: sec-001-2-observations-and-reductions
section_title: "Observations and reductions"
section_number: 2
pages: 2-3
source_pdf: 0203462v1.pdf
source_sha256: 337c24b051365f0a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.863
doc_brief: "arXiv:astro-ph/0203462v1 26 Mar 2002 — We present a high-resolution (R=75,000, S/N ∼500) spectroscopic analysis of the bright (V=11.7), extreme halo giant CS 31082-001 ([Fe/H] = −2.9), obtained in an"
---
[]{#observations label="observations"}

CS 31082-001 was first observed at high dispersion (R$>$<!-- -->45,000) with the new ESO-VLT spectrograph UVES (Dekker et al. [@dekker00]) in August 2000, and was immediately found to display outstandingly strong europium and thorium lines. The star was promptly re-observed at the highest possible resolution ($R=75,000$ in the blue arm of the spectrograph) during a subsequent night, and again in October 2000. Most of the spectra were obtained simultaneously in both the blue and red arms of UVES, using a dichroic mirror, as summarized in Table [\[T-log\]](#T-log){reference-type="ref" reference="T-log"}.

::: table*
  ------------ ----------- ----------- ----------------------------------- ----------------- ------------------------------------ ----------------- -----------------------
  Date         MJD          Exp. time   $\lambda_{start} - \lambda_{end}$   Resolving Power   $\lambda_{start} -  \lambda_{end}$   Resolving Power   V$_{r\: barycentric}$
               \(s\)          Blue                     Red                                                                                          
  2000/08/06   51763.396      1,200                 335-456nm                   45,000                    480-680nm                    45,000               139.03
  2000/08/06   51763.412      1,200                 335-456nm                   45,000                    670-900nm                    45,000       
  2000/08/10   51767.281      3,000              335-456nm$^{*}$                 70000                        --                         --         
  2000/08/10   51767.317      3,000              335-456nm$^{*}$                 70000                        --                         --         
  2000/10/11   51829.169      7,200                 310-390nm                   77,000                        --                         --         
  2000/10/14   51832.176      3,600                 310-390nm                   77,000                    480-680nm                    86,000               139.10
  2000/10/14   51832.219      3,600                 310-390nm                   77,000                    480-680nm                    86,000               139.14
  2000/10/15   51833.223      3,600                 310-390nm                   77,000                    480-680nm                    86,000               139.08
  2000/10/17   51835.147      3,600                 380-510nm                   75,000                    680-1000nm                   86,000       
  2000/10/19   51837.184      3,600                 380-510nm                   75,000                    680-1000nm                   86,000       
  ------------ ----------- ----------- ----------------------------------- ----------------- ------------------------------------ ----------------- -----------------------

$^{*}$: obtained with Image Slicer

  ------------ --------------- --------------- --------- --------- --------- --------- --------- ---------
  Setting           Total        S/N per pixel                                                   
                Exp. time (s)          \@310nm   \@350nm   \@390nm   \@420nm   \@490nm   \@630nm   \@800nm
  310-390nm        18,000                   35       150       350                               
  335-460nm         6,000                            110       250       300                     
  380-510nm         7,200                                      250       250       200           
  480-680nm        10,800                                                          250       340 
  670-1000nm        7,200                                                                              110
  ------------ --------------- --------------- --------- --------- --------- --------- --------- ---------
:::

Reductions were performed using the UVES context within MIDAS. The succession of tasks included bias subtraction from all images, fit and subtraction of the inter-order background from the object and flat-field images, and the averaging of ten flat-fields per night into a master frame. The echelle orders of the object were optimally extracted[^1] (assuming a Gaussian profile for the object perpendicular to the dispersion, and a constant for the sky background); the same weights were applied to extract the flat-field, which was then used to correct both for pixel-to-pixel variations and the blaze of the instrument. The wavelength calibration was performed on Th-Ar lamp frames and applied to the extracted object. The spectra were finally resampled to a constant wavelength step and normalized to unity by fitting a spline function. All spectra obtained with identical spectrograph settings (same cross-disperser and same central wavelength) were then co-added after radial-velocity correction. The lower part of Table [\[T-log\]](#T-log){reference-type="ref" reference="T-log"} summarizes the obtained signal-to-noise ratio per pixel (1 pixel$\sim$<!-- -->0.0015nm) at wavelengths of interest.

Radial velocities given in the table are only those computed from the 480-580nm red spectra (which permitted corrections for small instrumental shifts from the telluric absorption lines). In addition to the spectra reported here, we took exposures of CS 31082-001 with UVES again in September 2001 (5-9 september) and the radial velocity was still impressively unchanged (mean of four measurements in 2001 V$_{r\:
barycentric}=139.05\pm0.05 kms^{-1}$) and Aoki (2002, private communication) found V$_{r\:barycentric}=138.9\pm0.24 kms^{-1}$ from observations with HDS on the Subaru telescope. There is therefore *no sign* of radial velocity variations in this star, and hence *no hint that CS 31082-001 could be a binary*.

[^1]: In the two frames that were obtained through the image slicer, the extraction was simply an average of all pixels in the object profile, spread over four slices.
