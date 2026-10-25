# mini-health-warehouse

This program is to demonstrate my technical and domain expertise in the data engineering pipeline for the medical claims space. 

## Bronze Layer - Medicare Claims Data 
I used a python program to generate randomized, dummy data to mirror the structure and fields we get from CMS. This information bares the same complications we find in normal CCLF batches, including - 
- Claims split between Professional and Facility (DME is excluded for this demo) with different processed fields.
- Claims finalizations and adjustments between CCLFs - so new batches should incrementally update prior rows. 
- Spread out diagnosis and procedure billing information across multiple columns (dx_cd1, dx_cd2, admtgn_dgns_cd).

## Silver Layer 
