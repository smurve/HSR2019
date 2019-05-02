import sys
import math
import numpy as np
import tensorflow as tf
import inspect
import os

# A little tool stolen from Magnus Erik Hvass Pedersen
def print_progress(format_string, count, total=1.0):

    pct_complete = float(count) / total
    format_string = "\r"+ format_string
    msg = format_string.format(pct_complete)

    sys.stdout.write(msg)
    sys.stdout.flush()
    
    
# returns an np.array the size of 'array' with booleans True if that value in array is included in 'values'
def array_in(array, values):
    return np.array([ 
        np.array([ j[0] == i[0] and j[1] == i[1] 
                  for i in values]).any() 
        for j in array ])

def one_hot(df, size):
    ords = list(df)
    return np.transpose(np.eye(size)[ords])

def one_hot(df, size):
    ords = list(df)
    return np.transpose(np.eye(size)[ords])


def create_input_data(df, select_feats=[], oh_feats={}, cross_feats=[]):    
    """
    create a list of input columns from pandas raw data
    df: a pandas dataframe containing raw input data
    select_feats: an array containing the names of features to be selected without transformation
    oh_feats: a dictionary containing the names and sizes of discrete numerical features that are to be one-hot encoded
    cross_feats: a list of oh_feats consisting of two discrete features to cross
    """

    def _safe_append(l, r):
        if l == [] or l is None:
            return r
        else:
            return np.append(l, r, axis=0)

    res = [list(df[n]) for n in select_feats]
    
    for k in oh_feats:
        res = _safe_append(res, one_hot(df[k], oh_feats[k]))

    for c in cross_feats:
        keys = list(c.keys())
        keys.sort()
        
        lk, ls = keys[0], c[keys[0]]
        rk, rs = keys[1], c[keys[1]]
        lhs = one_hot(df[lk], ls)
        rhs = one_hot(df[rk], rs)
        cross = [(lhs[:,i].reshape(ls,1) * rhs[:,i].reshape(1,rs)).reshape(rs*ls) for i in range(len(df))]
        cross = np.transpose(cross)
        res = _safe_append(res, cross)

    return res


    
def haversine(origin, destination):
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    origin : tuple of float
        (lat, long)
    destination : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d



def tf_haversine(lat1, lon1, lat2, lon2):
    
    def radians(a):
        return a * math.pi / 180.0

    radius = 6371.0
    dlat = radians (lat2 - lat1) 
    dlon = radians (lon2 - lon1)
    a = (tf.sin(dlat / 2.0) * tf.sin(dlat/2.0) +
         tf.cos(radians(lat1)) * tf.cos(radians(lat2)) *
         tf.sin(dlon / 2.0) * tf.sin(dlon / 2.0))
    c = 2.0 * tf.atan2(tf.sqrt(a), tf.sqrt(1.0 - a))
    return radius * c


def make_src_dumper(package):
    def write_py(func):
        filename=os.path.join(package, "{}.py".format(func.__name__))
        with open(filename, 'w') as file:
            file.write(inspect.getsource(func))
        return "{} written to {}.".format(func.__name__, filename)
    return write_py

def create_runpy(filename, args):
    export = "export PYTHONPATH=${PYTHONPATH}:${PWD}\n"
    python = "python -m train.task \\\n"
    _args = "".join(['  --{}="{}"  \\\n'.format(key, value) for key, value in args.items() if value != False])
    with open(filename, 'w') as f:
        f.write(export+python+_args)
    