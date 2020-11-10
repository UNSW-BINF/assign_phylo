def UPGMA(distances):
    """Unweighted pair group method with arithmetic mean (UPGMA) agglomerative clustering.
    
    Parameters
    ----------
    distances: np.ndarray
        A two dimensional, square, symmetric matrix containing distances between data
        points. The diagonal is zeros.
        
    Returns
    -------
    np.ndarray
        The linkage matrix, as specified in scipy. Briefly, this should be a 2d matrix
        each row containing 4 elements. The first and second element should denote the
        cluster IDs being merged, the third element should be the distance, and the
        fourth element should be the number of elements within this new cluster. Any
        new cluster should be assigned an incrementing ID, e.g. after the first step
        where the first two points are merged into a cluster, the new cluster ID should
        be N, then N+1, N+2, ... in subsequent steps.
        
    Notes
    -----
    You can validate your implementation to scipy's `cluster.hierarchy.linkage`
    function using average linkage. UPGMA and average linkage agglomerative clustering
    are the same thing. Your function should return identical results in all cases.
    
    """
    raise NotImplementedError()
        
        
def jukes_cantor(p: float) -> float:
    """The Jukes-Cantor correction for estimating genetic distances.
    
    Parameters
    ----------
    p: float
        The proportional distance, i.e. the number of of mismatching symbols (Hamming
        distance) divided by the total sequence length.
        
    Returns
    -------
    float
        The corrected genetic distance.
    
    """
    raise NotImplementedError()
