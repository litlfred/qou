---
doc_id: 0510388v1
doc_title: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space"
section_id: sec-020-17-the-method-of-moving-frames-in-s3
section_title: "The method of moving frames in S3 ."
section_number: 17
pages: 40-43
source_pdf: 0510388v1.pdf
source_sha256: c83c0f6a2eaa74f3
toc_source: inferred
doc_brief: "Electrodynamics and the Gauss linking integral on the 3-sphere and in hyperbolic 3-space — 64 sections: Front matter; ORGANIZATION; STATEMENTS OF RESULTS"
---
The computations which lead to the various integral formulas on  S3  in parallel 
transport format will be carried out using "moving frames" which are obtained via 
parallel transport from a single orthonormal frame, as follows. 
 
Let  x  =  (1, 0, 0, 0) ,  and let  X1 ,  X2 ,  X3  be the usual orthonormal basis for the 
tangent space  TxS3  to  S3  at  x . 
                                            
For each point  y  =  (y0 , y1 , y2 , y3)  ≠  — x  in  S3
 ,  we parallel transport this 
orthonormal basis for  TxS3  along the unique shortest geodesic (great circle arc) 
from  x  to  y  to obtain an orthonormal basis 
 
E1  =  PyxX1 ,   E2  =  PyxX2 ,   E3  =  PyxX3 
 
for  TyS3 .   
                                      
 
                                                    Moving frames 
 
 
 
 
 
 
Using the formula for  PyxV  from the previous section, we calculate that 
 
                 E1  =  (— y1 ,  1  —  y1
2/(1 + y0) ,  — y1y2/(1 + y0) ,  — y1y3/(1 + y0))  
 
                 E2  =  (— y2 ,  — y1y2/(1 + y0) ,  1  —  y2
2/(1 + y0) ,  — y2y3/(1 + y0)) 
 
                 E3  =  (— y3 ,  — y1y3/(1 + y0) ,  — y2y3/(1 + y0) ,  1  —  y3
2/(1 + y0)) . 
 
 
Next, let  θ1 ,  θ2 ,  θ3  denote the 1-forms on  S3  —  {—x}  which are dual to 
E1 ,  E2 ,  E3 ,  in the sense that  θi(V)  =  < Ei , V >  for all vectors  V  and for 
i  =  1, 2, 3. 
 
We can write 
 
    θ1  =  — y1 dy0  +  (1  —  y1
2/(1 + y0)) dy1  —  y1y2/(1 + y0) dy2  —  y1y3/(1 + y0) dy3 
 
    θ2  =  — y2 dy0  —  y1y2/(1 + y0) dy1  +  (1  —  y2
2/(1 + y0)) dy2  —  y2y3/(1 + y0) dy3 
 
    θ3  =  — y3 dy0  —  y1y3/(1 + y0) dy1  —  y2y3/(1 + y0) dy2  +  (1  —  y3
2/(1 + y0)) dy3 , 
 
where we understand the right hand sides as restricted to  S3 . 
 
Since   y0
2  +  y1
2  +  y2
2  +  y3
2  =  1   on  S3 ,  we can add a fourth equation to the 
three above, 
 
    0  =  y0 dy0  +  y1 dy1  +  y2 dy2  +  y3 dy3 . 
 
 
 
 
 
 
Using this fourth equation, we can simplify the first three to read 
 
    θ1  =  — y1/(1 + y0) dy0  +  dy1 
 
    θ2  =  — y2/(1 + y0) dy0  +  dy2 
 
    θ3  =  — y3/(1 + y0) dy0  +  dy3 . 
 
 
We then invert this system to obtain 
 
    dy0  =  — y1 θ1  —  y2 θ2  —  y3 θ3 
 
    dy1  =  θ1  —  (y1/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) 
 
    dy2  =  θ2  —  (y2/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) 
 
    dy3  =  θ3  —  (y3/(1 + y0)) (y1 θ1  +  y2 θ2  +  y3 θ3) . 
 
 
With these equations in hand, we easily obtain 
 
    dθ1  =  y2/(1 + y0)  θ1 ∧ θ2  —  y3/(1 + y0)  θ3 ∧ θ1 
 
    dθ2  =  y3/(1 + y0)  θ2 ∧ θ3  —  y1/(1 + y0)  θ1 ∧ θ2 
 
    dθ3  =  y1/(1 + y0)  θ3 ∧ θ1  —  y2/(1 + y0)  θ2 ∧ θ3 .
