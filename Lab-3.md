

```python
import ctypes
from pympler import asizeof

class DynamicArray:
    def getsize(self):
        import sys
        return sys.getsizeof(self._A)
    
    def ToString(self):
        for i in self._A:
            print(i," ")
            
    def getLength(self):
        return len(self._A)
    
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A=self._make_array(self._capacity)
        
    def __len__(self):
        return self._n
    
    def __getitem__(self,k):
        if not 0 <= k <self._n:
            raise IndexError('invalid index')
        return self._A[k]
    
    def append(self,obj):
        if self._n == self._capacity: #kapasite yeterli degilse, kapasiteyi 2'ye katla.
            self._resize(2*self._capacity)
        self._A[self._n]=obj
        self._n+=1
        
    def _resize(self, c): # nonpublic utitity
        print("şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...")
        B = self._make_array(c) # new (bigger) array
        for k in range(self._n): # for each existing value
            B[k] = self._A[k]
        self._A=B # use the bigger array
        self._capacity = c
        
    def _make_array(self, c): # nonpublic utitity
        return(c*ctypes.py_object)()
```


```python
myArray = DynamicArray()
for i in range(512):
    myArray.append(i)
    print(i," eklendi. ---> Array size: ",myArray.__len__()," Array Length: ",myArray.getLength())
```

    0  eklendi. ---> Array size:  1  Array Length:  1
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    1  eklendi. ---> Array size:  2  Array Length:  2
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    2  eklendi. ---> Array size:  3  Array Length:  4
    3  eklendi. ---> Array size:  4  Array Length:  4
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    4  eklendi. ---> Array size:  5  Array Length:  8
    5  eklendi. ---> Array size:  6  Array Length:  8
    6  eklendi. ---> Array size:  7  Array Length:  8
    7  eklendi. ---> Array size:  8  Array Length:  8
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    8  eklendi. ---> Array size:  9  Array Length:  16
    9  eklendi. ---> Array size:  10  Array Length:  16
    10  eklendi. ---> Array size:  11  Array Length:  16
    11  eklendi. ---> Array size:  12  Array Length:  16
    12  eklendi. ---> Array size:  13  Array Length:  16
    13  eklendi. ---> Array size:  14  Array Length:  16
    14  eklendi. ---> Array size:  15  Array Length:  16
    15  eklendi. ---> Array size:  16  Array Length:  16
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    16  eklendi. ---> Array size:  17  Array Length:  32
    17  eklendi. ---> Array size:  18  Array Length:  32
    18  eklendi. ---> Array size:  19  Array Length:  32
    19  eklendi. ---> Array size:  20  Array Length:  32
    20  eklendi. ---> Array size:  21  Array Length:  32
    21  eklendi. ---> Array size:  22  Array Length:  32
    22  eklendi. ---> Array size:  23  Array Length:  32
    23  eklendi. ---> Array size:  24  Array Length:  32
    24  eklendi. ---> Array size:  25  Array Length:  32
    25  eklendi. ---> Array size:  26  Array Length:  32
    26  eklendi. ---> Array size:  27  Array Length:  32
    27  eklendi. ---> Array size:  28  Array Length:  32
    28  eklendi. ---> Array size:  29  Array Length:  32
    29  eklendi. ---> Array size:  30  Array Length:  32
    30  eklendi. ---> Array size:  31  Array Length:  32
    31  eklendi. ---> Array size:  32  Array Length:  32
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    32  eklendi. ---> Array size:  33  Array Length:  64
    33  eklendi. ---> Array size:  34  Array Length:  64
    34  eklendi. ---> Array size:  35  Array Length:  64
    35  eklendi. ---> Array size:  36  Array Length:  64
    36  eklendi. ---> Array size:  37  Array Length:  64
    37  eklendi. ---> Array size:  38  Array Length:  64
    38  eklendi. ---> Array size:  39  Array Length:  64
    39  eklendi. ---> Array size:  40  Array Length:  64
    40  eklendi. ---> Array size:  41  Array Length:  64
    41  eklendi. ---> Array size:  42  Array Length:  64
    42  eklendi. ---> Array size:  43  Array Length:  64
    43  eklendi. ---> Array size:  44  Array Length:  64
    44  eklendi. ---> Array size:  45  Array Length:  64
    45  eklendi. ---> Array size:  46  Array Length:  64
    46  eklendi. ---> Array size:  47  Array Length:  64
    47  eklendi. ---> Array size:  48  Array Length:  64
    48  eklendi. ---> Array size:  49  Array Length:  64
    49  eklendi. ---> Array size:  50  Array Length:  64
    50  eklendi. ---> Array size:  51  Array Length:  64
    51  eklendi. ---> Array size:  52  Array Length:  64
    52  eklendi. ---> Array size:  53  Array Length:  64
    53  eklendi. ---> Array size:  54  Array Length:  64
    54  eklendi. ---> Array size:  55  Array Length:  64
    55  eklendi. ---> Array size:  56  Array Length:  64
    56  eklendi. ---> Array size:  57  Array Length:  64
    57  eklendi. ---> Array size:  58  Array Length:  64
    58  eklendi. ---> Array size:  59  Array Length:  64
    59  eklendi. ---> Array size:  60  Array Length:  64
    60  eklendi. ---> Array size:  61  Array Length:  64
    61  eklendi. ---> Array size:  62  Array Length:  64
    62  eklendi. ---> Array size:  63  Array Length:  64
    63  eklendi. ---> Array size:  64  Array Length:  64
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    64  eklendi. ---> Array size:  65  Array Length:  128
    65  eklendi. ---> Array size:  66  Array Length:  128
    66  eklendi. ---> Array size:  67  Array Length:  128
    67  eklendi. ---> Array size:  68  Array Length:  128
    68  eklendi. ---> Array size:  69  Array Length:  128
    69  eklendi. ---> Array size:  70  Array Length:  128
    70  eklendi. ---> Array size:  71  Array Length:  128
    71  eklendi. ---> Array size:  72  Array Length:  128
    72  eklendi. ---> Array size:  73  Array Length:  128
    73  eklendi. ---> Array size:  74  Array Length:  128
    74  eklendi. ---> Array size:  75  Array Length:  128
    75  eklendi. ---> Array size:  76  Array Length:  128
    76  eklendi. ---> Array size:  77  Array Length:  128
    77  eklendi. ---> Array size:  78  Array Length:  128
    78  eklendi. ---> Array size:  79  Array Length:  128
    79  eklendi. ---> Array size:  80  Array Length:  128
    80  eklendi. ---> Array size:  81  Array Length:  128
    81  eklendi. ---> Array size:  82  Array Length:  128
    82  eklendi. ---> Array size:  83  Array Length:  128
    83  eklendi. ---> Array size:  84  Array Length:  128
    84  eklendi. ---> Array size:  85  Array Length:  128
    85  eklendi. ---> Array size:  86  Array Length:  128
    86  eklendi. ---> Array size:  87  Array Length:  128
    87  eklendi. ---> Array size:  88  Array Length:  128
    88  eklendi. ---> Array size:  89  Array Length:  128
    89  eklendi. ---> Array size:  90  Array Length:  128
    90  eklendi. ---> Array size:  91  Array Length:  128
    91  eklendi. ---> Array size:  92  Array Length:  128
    92  eklendi. ---> Array size:  93  Array Length:  128
    93  eklendi. ---> Array size:  94  Array Length:  128
    94  eklendi. ---> Array size:  95  Array Length:  128
    95  eklendi. ---> Array size:  96  Array Length:  128
    96  eklendi. ---> Array size:  97  Array Length:  128
    97  eklendi. ---> Array size:  98  Array Length:  128
    98  eklendi. ---> Array size:  99  Array Length:  128
    99  eklendi. ---> Array size:  100  Array Length:  128
    100  eklendi. ---> Array size:  101  Array Length:  128
    101  eklendi. ---> Array size:  102  Array Length:  128
    102  eklendi. ---> Array size:  103  Array Length:  128
    103  eklendi. ---> Array size:  104  Array Length:  128
    104  eklendi. ---> Array size:  105  Array Length:  128
    105  eklendi. ---> Array size:  106  Array Length:  128
    106  eklendi. ---> Array size:  107  Array Length:  128
    107  eklendi. ---> Array size:  108  Array Length:  128
    108  eklendi. ---> Array size:  109  Array Length:  128
    109  eklendi. ---> Array size:  110  Array Length:  128
    110  eklendi. ---> Array size:  111  Array Length:  128
    111  eklendi. ---> Array size:  112  Array Length:  128
    112  eklendi. ---> Array size:  113  Array Length:  128
    113  eklendi. ---> Array size:  114  Array Length:  128
    114  eklendi. ---> Array size:  115  Array Length:  128
    115  eklendi. ---> Array size:  116  Array Length:  128
    116  eklendi. ---> Array size:  117  Array Length:  128
    117  eklendi. ---> Array size:  118  Array Length:  128
    118  eklendi. ---> Array size:  119  Array Length:  128
    119  eklendi. ---> Array size:  120  Array Length:  128
    120  eklendi. ---> Array size:  121  Array Length:  128
    121  eklendi. ---> Array size:  122  Array Length:  128
    122  eklendi. ---> Array size:  123  Array Length:  128
    123  eklendi. ---> Array size:  124  Array Length:  128
    124  eklendi. ---> Array size:  125  Array Length:  128
    125  eklendi. ---> Array size:  126  Array Length:  128
    126  eklendi. ---> Array size:  127  Array Length:  128
    127  eklendi. ---> Array size:  128  Array Length:  128
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    128  eklendi. ---> Array size:  129  Array Length:  256
    129  eklendi. ---> Array size:  130  Array Length:  256
    130  eklendi. ---> Array size:  131  Array Length:  256
    131  eklendi. ---> Array size:  132  Array Length:  256
    132  eklendi. ---> Array size:  133  Array Length:  256
    133  eklendi. ---> Array size:  134  Array Length:  256
    134  eklendi. ---> Array size:  135  Array Length:  256
    135  eklendi. ---> Array size:  136  Array Length:  256
    136  eklendi. ---> Array size:  137  Array Length:  256
    137  eklendi. ---> Array size:  138  Array Length:  256
    138  eklendi. ---> Array size:  139  Array Length:  256
    139  eklendi. ---> Array size:  140  Array Length:  256
    140  eklendi. ---> Array size:  141  Array Length:  256
    141  eklendi. ---> Array size:  142  Array Length:  256
    142  eklendi. ---> Array size:  143  Array Length:  256
    143  eklendi. ---> Array size:  144  Array Length:  256
    144  eklendi. ---> Array size:  145  Array Length:  256
    145  eklendi. ---> Array size:  146  Array Length:  256
    146  eklendi. ---> Array size:  147  Array Length:  256
    147  eklendi. ---> Array size:  148  Array Length:  256
    148  eklendi. ---> Array size:  149  Array Length:  256
    149  eklendi. ---> Array size:  150  Array Length:  256
    150  eklendi. ---> Array size:  151  Array Length:  256
    151  eklendi. ---> Array size:  152  Array Length:  256
    152  eklendi. ---> Array size:  153  Array Length:  256
    153  eklendi. ---> Array size:  154  Array Length:  256
    154  eklendi. ---> Array size:  155  Array Length:  256
    155  eklendi. ---> Array size:  156  Array Length:  256
    156  eklendi. ---> Array size:  157  Array Length:  256
    157  eklendi. ---> Array size:  158  Array Length:  256
    158  eklendi. ---> Array size:  159  Array Length:  256
    159  eklendi. ---> Array size:  160  Array Length:  256
    160  eklendi. ---> Array size:  161  Array Length:  256
    161  eklendi. ---> Array size:  162  Array Length:  256
    162  eklendi. ---> Array size:  163  Array Length:  256
    163  eklendi. ---> Array size:  164  Array Length:  256
    164  eklendi. ---> Array size:  165  Array Length:  256
    165  eklendi. ---> Array size:  166  Array Length:  256
    166  eklendi. ---> Array size:  167  Array Length:  256
    167  eklendi. ---> Array size:  168  Array Length:  256
    168  eklendi. ---> Array size:  169  Array Length:  256
    169  eklendi. ---> Array size:  170  Array Length:  256
    170  eklendi. ---> Array size:  171  Array Length:  256
    171  eklendi. ---> Array size:  172  Array Length:  256
    172  eklendi. ---> Array size:  173  Array Length:  256
    173  eklendi. ---> Array size:  174  Array Length:  256
    174  eklendi. ---> Array size:  175  Array Length:  256
    175  eklendi. ---> Array size:  176  Array Length:  256
    176  eklendi. ---> Array size:  177  Array Length:  256
    177  eklendi. ---> Array size:  178  Array Length:  256
    178  eklendi. ---> Array size:  179  Array Length:  256
    179  eklendi. ---> Array size:  180  Array Length:  256
    180  eklendi. ---> Array size:  181  Array Length:  256
    181  eklendi. ---> Array size:  182  Array Length:  256
    182  eklendi. ---> Array size:  183  Array Length:  256
    183  eklendi. ---> Array size:  184  Array Length:  256
    184  eklendi. ---> Array size:  185  Array Length:  256
    185  eklendi. ---> Array size:  186  Array Length:  256
    186  eklendi. ---> Array size:  187  Array Length:  256
    187  eklendi. ---> Array size:  188  Array Length:  256
    188  eklendi. ---> Array size:  189  Array Length:  256
    189  eklendi. ---> Array size:  190  Array Length:  256
    190  eklendi. ---> Array size:  191  Array Length:  256
    191  eklendi. ---> Array size:  192  Array Length:  256
    192  eklendi. ---> Array size:  193  Array Length:  256
    193  eklendi. ---> Array size:  194  Array Length:  256
    194  eklendi. ---> Array size:  195  Array Length:  256
    195  eklendi. ---> Array size:  196  Array Length:  256
    196  eklendi. ---> Array size:  197  Array Length:  256
    197  eklendi. ---> Array size:  198  Array Length:  256
    198  eklendi. ---> Array size:  199  Array Length:  256
    199  eklendi. ---> Array size:  200  Array Length:  256
    200  eklendi. ---> Array size:  201  Array Length:  256
    201  eklendi. ---> Array size:  202  Array Length:  256
    202  eklendi. ---> Array size:  203  Array Length:  256
    203  eklendi. ---> Array size:  204  Array Length:  256
    204  eklendi. ---> Array size:  205  Array Length:  256
    205  eklendi. ---> Array size:  206  Array Length:  256
    206  eklendi. ---> Array size:  207  Array Length:  256
    207  eklendi. ---> Array size:  208  Array Length:  256
    208  eklendi. ---> Array size:  209  Array Length:  256
    209  eklendi. ---> Array size:  210  Array Length:  256
    210  eklendi. ---> Array size:  211  Array Length:  256
    211  eklendi. ---> Array size:  212  Array Length:  256
    212  eklendi. ---> Array size:  213  Array Length:  256
    213  eklendi. ---> Array size:  214  Array Length:  256
    214  eklendi. ---> Array size:  215  Array Length:  256
    215  eklendi. ---> Array size:  216  Array Length:  256
    216  eklendi. ---> Array size:  217  Array Length:  256
    217  eklendi. ---> Array size:  218  Array Length:  256
    218  eklendi. ---> Array size:  219  Array Length:  256
    219  eklendi. ---> Array size:  220  Array Length:  256
    220  eklendi. ---> Array size:  221  Array Length:  256
    221  eklendi. ---> Array size:  222  Array Length:  256
    222  eklendi. ---> Array size:  223  Array Length:  256
    223  eklendi. ---> Array size:  224  Array Length:  256
    224  eklendi. ---> Array size:  225  Array Length:  256
    225  eklendi. ---> Array size:  226  Array Length:  256
    226  eklendi. ---> Array size:  227  Array Length:  256
    227  eklendi. ---> Array size:  228  Array Length:  256
    228  eklendi. ---> Array size:  229  Array Length:  256
    229  eklendi. ---> Array size:  230  Array Length:  256
    230  eklendi. ---> Array size:  231  Array Length:  256
    231  eklendi. ---> Array size:  232  Array Length:  256
    232  eklendi. ---> Array size:  233  Array Length:  256
    233  eklendi. ---> Array size:  234  Array Length:  256
    234  eklendi. ---> Array size:  235  Array Length:  256
    235  eklendi. ---> Array size:  236  Array Length:  256
    236  eklendi. ---> Array size:  237  Array Length:  256
    237  eklendi. ---> Array size:  238  Array Length:  256
    238  eklendi. ---> Array size:  239  Array Length:  256
    239  eklendi. ---> Array size:  240  Array Length:  256
    240  eklendi. ---> Array size:  241  Array Length:  256
    241  eklendi. ---> Array size:  242  Array Length:  256
    242  eklendi. ---> Array size:  243  Array Length:  256
    243  eklendi. ---> Array size:  244  Array Length:  256
    244  eklendi. ---> Array size:  245  Array Length:  256
    245  eklendi. ---> Array size:  246  Array Length:  256
    246  eklendi. ---> Array size:  247  Array Length:  256
    247  eklendi. ---> Array size:  248  Array Length:  256
    248  eklendi. ---> Array size:  249  Array Length:  256
    249  eklendi. ---> Array size:  250  Array Length:  256
    250  eklendi. ---> Array size:  251  Array Length:  256
    251  eklendi. ---> Array size:  252  Array Length:  256
    252  eklendi. ---> Array size:  253  Array Length:  256
    253  eklendi. ---> Array size:  254  Array Length:  256
    254  eklendi. ---> Array size:  255  Array Length:  256
    255  eklendi. ---> Array size:  256  Array Length:  256
    şu an worst-case durumunda, liste dolu, başka yerken n*2 lik yer alınıp, taşıma yapılacak...
    256  eklendi. ---> Array size:  257  Array Length:  512
    257  eklendi. ---> Array size:  258  Array Length:  512
    258  eklendi. ---> Array size:  259  Array Length:  512
    259  eklendi. ---> Array size:  260  Array Length:  512
    260  eklendi. ---> Array size:  261  Array Length:  512
    261  eklendi. ---> Array size:  262  Array Length:  512
    262  eklendi. ---> Array size:  263  Array Length:  512
    263  eklendi. ---> Array size:  264  Array Length:  512
    264  eklendi. ---> Array size:  265  Array Length:  512
    265  eklendi. ---> Array size:  266  Array Length:  512
    266  eklendi. ---> Array size:  267  Array Length:  512
    267  eklendi. ---> Array size:  268  Array Length:  512
    268  eklendi. ---> Array size:  269  Array Length:  512
    269  eklendi. ---> Array size:  270  Array Length:  512
    270  eklendi. ---> Array size:  271  Array Length:  512
    271  eklendi. ---> Array size:  272  Array Length:  512
    272  eklendi. ---> Array size:  273  Array Length:  512
    273  eklendi. ---> Array size:  274  Array Length:  512
    274  eklendi. ---> Array size:  275  Array Length:  512
    275  eklendi. ---> Array size:  276  Array Length:  512
    276  eklendi. ---> Array size:  277  Array Length:  512
    277  eklendi. ---> Array size:  278  Array Length:  512
    278  eklendi. ---> Array size:  279  Array Length:  512
    279  eklendi. ---> Array size:  280  Array Length:  512
    280  eklendi. ---> Array size:  281  Array Length:  512
    281  eklendi. ---> Array size:  282  Array Length:  512
    282  eklendi. ---> Array size:  283  Array Length:  512
    283  eklendi. ---> Array size:  284  Array Length:  512
    284  eklendi. ---> Array size:  285  Array Length:  512
    285  eklendi. ---> Array size:  286  Array Length:  512
    286  eklendi. ---> Array size:  287  Array Length:  512
    287  eklendi. ---> Array size:  288  Array Length:  512
    288  eklendi. ---> Array size:  289  Array Length:  512
    289  eklendi. ---> Array size:  290  Array Length:  512
    290  eklendi. ---> Array size:  291  Array Length:  512
    291  eklendi. ---> Array size:  292  Array Length:  512
    292  eklendi. ---> Array size:  293  Array Length:  512
    293  eklendi. ---> Array size:  294  Array Length:  512
    294  eklendi. ---> Array size:  295  Array Length:  512
    295  eklendi. ---> Array size:  296  Array Length:  512
    296  eklendi. ---> Array size:  297  Array Length:  512
    297  eklendi. ---> Array size:  298  Array Length:  512
    298  eklendi. ---> Array size:  299  Array Length:  512
    299  eklendi. ---> Array size:  300  Array Length:  512
    300  eklendi. ---> Array size:  301  Array Length:  512
    301  eklendi. ---> Array size:  302  Array Length:  512
    302  eklendi. ---> Array size:  303  Array Length:  512
    303  eklendi. ---> Array size:  304  Array Length:  512
    304  eklendi. ---> Array size:  305  Array Length:  512
    305  eklendi. ---> Array size:  306  Array Length:  512
    306  eklendi. ---> Array size:  307  Array Length:  512
    307  eklendi. ---> Array size:  308  Array Length:  512
    308  eklendi. ---> Array size:  309  Array Length:  512
    309  eklendi. ---> Array size:  310  Array Length:  512
    310  eklendi. ---> Array size:  311  Array Length:  512
    311  eklendi. ---> Array size:  312  Array Length:  512
    312  eklendi. ---> Array size:  313  Array Length:  512
    313  eklendi. ---> Array size:  314  Array Length:  512
    314  eklendi. ---> Array size:  315  Array Length:  512
    315  eklendi. ---> Array size:  316  Array Length:  512
    316  eklendi. ---> Array size:  317  Array Length:  512
    317  eklendi. ---> Array size:  318  Array Length:  512
    318  eklendi. ---> Array size:  319  Array Length:  512
    319  eklendi. ---> Array size:  320  Array Length:  512
    320  eklendi. ---> Array size:  321  Array Length:  512
    321  eklendi. ---> Array size:  322  Array Length:  512
    322  eklendi. ---> Array size:  323  Array Length:  512
    323  eklendi. ---> Array size:  324  Array Length:  512
    324  eklendi. ---> Array size:  325  Array Length:  512
    325  eklendi. ---> Array size:  326  Array Length:  512
    326  eklendi. ---> Array size:  327  Array Length:  512
    327  eklendi. ---> Array size:  328  Array Length:  512
    328  eklendi. ---> Array size:  329  Array Length:  512
    329  eklendi. ---> Array size:  330  Array Length:  512
    330  eklendi. ---> Array size:  331  Array Length:  512
    331  eklendi. ---> Array size:  332  Array Length:  512
    332  eklendi. ---> Array size:  333  Array Length:  512
    333  eklendi. ---> Array size:  334  Array Length:  512
    334  eklendi. ---> Array size:  335  Array Length:  512
    335  eklendi. ---> Array size:  336  Array Length:  512
    336  eklendi. ---> Array size:  337  Array Length:  512
    337  eklendi. ---> Array size:  338  Array Length:  512
    338  eklendi. ---> Array size:  339  Array Length:  512
    339  eklendi. ---> Array size:  340  Array Length:  512
    340  eklendi. ---> Array size:  341  Array Length:  512
    341  eklendi. ---> Array size:  342  Array Length:  512
    342  eklendi. ---> Array size:  343  Array Length:  512
    343  eklendi. ---> Array size:  344  Array Length:  512
    344  eklendi. ---> Array size:  345  Array Length:  512
    345  eklendi. ---> Array size:  346  Array Length:  512
    346  eklendi. ---> Array size:  347  Array Length:  512
    347  eklendi. ---> Array size:  348  Array Length:  512
    348  eklendi. ---> Array size:  349  Array Length:  512
    349  eklendi. ---> Array size:  350  Array Length:  512
    350  eklendi. ---> Array size:  351  Array Length:  512
    351  eklendi. ---> Array size:  352  Array Length:  512
    352  eklendi. ---> Array size:  353  Array Length:  512
    353  eklendi. ---> Array size:  354  Array Length:  512
    354  eklendi. ---> Array size:  355  Array Length:  512
    355  eklendi. ---> Array size:  356  Array Length:  512
    356  eklendi. ---> Array size:  357  Array Length:  512
    357  eklendi. ---> Array size:  358  Array Length:  512
    358  eklendi. ---> Array size:  359  Array Length:  512
    359  eklendi. ---> Array size:  360  Array Length:  512
    360  eklendi. ---> Array size:  361  Array Length:  512
    361  eklendi. ---> Array size:  362  Array Length:  512
    362  eklendi. ---> Array size:  363  Array Length:  512
    363  eklendi. ---> Array size:  364  Array Length:  512
    364  eklendi. ---> Array size:  365  Array Length:  512
    365  eklendi. ---> Array size:  366  Array Length:  512
    366  eklendi. ---> Array size:  367  Array Length:  512
    367  eklendi. ---> Array size:  368  Array Length:  512
    368  eklendi. ---> Array size:  369  Array Length:  512
    369  eklendi. ---> Array size:  370  Array Length:  512
    370  eklendi. ---> Array size:  371  Array Length:  512
    371  eklendi. ---> Array size:  372  Array Length:  512
    372  eklendi. ---> Array size:  373  Array Length:  512
    373  eklendi. ---> Array size:  374  Array Length:  512
    374  eklendi. ---> Array size:  375  Array Length:  512
    375  eklendi. ---> Array size:  376  Array Length:  512
    376  eklendi. ---> Array size:  377  Array Length:  512
    377  eklendi. ---> Array size:  378  Array Length:  512
    378  eklendi. ---> Array size:  379  Array Length:  512
    379  eklendi. ---> Array size:  380  Array Length:  512
    380  eklendi. ---> Array size:  381  Array Length:  512
    381  eklendi. ---> Array size:  382  Array Length:  512
    382  eklendi. ---> Array size:  383  Array Length:  512
    383  eklendi. ---> Array size:  384  Array Length:  512
    384  eklendi. ---> Array size:  385  Array Length:  512
    385  eklendi. ---> Array size:  386  Array Length:  512
    386  eklendi. ---> Array size:  387  Array Length:  512
    387  eklendi. ---> Array size:  388  Array Length:  512
    388  eklendi. ---> Array size:  389  Array Length:  512
    389  eklendi. ---> Array size:  390  Array Length:  512
    390  eklendi. ---> Array size:  391  Array Length:  512
    391  eklendi. ---> Array size:  392  Array Length:  512
    392  eklendi. ---> Array size:  393  Array Length:  512
    393  eklendi. ---> Array size:  394  Array Length:  512
    394  eklendi. ---> Array size:  395  Array Length:  512
    395  eklendi. ---> Array size:  396  Array Length:  512
    396  eklendi. ---> Array size:  397  Array Length:  512
    397  eklendi. ---> Array size:  398  Array Length:  512
    398  eklendi. ---> Array size:  399  Array Length:  512
    399  eklendi. ---> Array size:  400  Array Length:  512
    400  eklendi. ---> Array size:  401  Array Length:  512
    401  eklendi. ---> Array size:  402  Array Length:  512
    402  eklendi. ---> Array size:  403  Array Length:  512
    403  eklendi. ---> Array size:  404  Array Length:  512
    404  eklendi. ---> Array size:  405  Array Length:  512
    405  eklendi. ---> Array size:  406  Array Length:  512
    406  eklendi. ---> Array size:  407  Array Length:  512
    407  eklendi. ---> Array size:  408  Array Length:  512
    408  eklendi. ---> Array size:  409  Array Length:  512
    409  eklendi. ---> Array size:  410  Array Length:  512
    410  eklendi. ---> Array size:  411  Array Length:  512
    411  eklendi. ---> Array size:  412  Array Length:  512
    412  eklendi. ---> Array size:  413  Array Length:  512
    413  eklendi. ---> Array size:  414  Array Length:  512
    414  eklendi. ---> Array size:  415  Array Length:  512
    415  eklendi. ---> Array size:  416  Array Length:  512
    416  eklendi. ---> Array size:  417  Array Length:  512
    417  eklendi. ---> Array size:  418  Array Length:  512
    418  eklendi. ---> Array size:  419  Array Length:  512
    419  eklendi. ---> Array size:  420  Array Length:  512
    420  eklendi. ---> Array size:  421  Array Length:  512
    421  eklendi. ---> Array size:  422  Array Length:  512
    422  eklendi. ---> Array size:  423  Array Length:  512
    423  eklendi. ---> Array size:  424  Array Length:  512
    424  eklendi. ---> Array size:  425  Array Length:  512
    425  eklendi. ---> Array size:  426  Array Length:  512
    426  eklendi. ---> Array size:  427  Array Length:  512
    427  eklendi. ---> Array size:  428  Array Length:  512
    428  eklendi. ---> Array size:  429  Array Length:  512
    429  eklendi. ---> Array size:  430  Array Length:  512
    430  eklendi. ---> Array size:  431  Array Length:  512
    431  eklendi. ---> Array size:  432  Array Length:  512
    432  eklendi. ---> Array size:  433  Array Length:  512
    433  eklendi. ---> Array size:  434  Array Length:  512
    434  eklendi. ---> Array size:  435  Array Length:  512
    435  eklendi. ---> Array size:  436  Array Length:  512
    436  eklendi. ---> Array size:  437  Array Length:  512
    437  eklendi. ---> Array size:  438  Array Length:  512
    438  eklendi. ---> Array size:  439  Array Length:  512
    439  eklendi. ---> Array size:  440  Array Length:  512
    440  eklendi. ---> Array size:  441  Array Length:  512
    441  eklendi. ---> Array size:  442  Array Length:  512
    442  eklendi. ---> Array size:  443  Array Length:  512
    443  eklendi. ---> Array size:  444  Array Length:  512
    444  eklendi. ---> Array size:  445  Array Length:  512
    445  eklendi. ---> Array size:  446  Array Length:  512
    446  eklendi. ---> Array size:  447  Array Length:  512
    447  eklendi. ---> Array size:  448  Array Length:  512
    448  eklendi. ---> Array size:  449  Array Length:  512
    449  eklendi. ---> Array size:  450  Array Length:  512
    450  eklendi. ---> Array size:  451  Array Length:  512
    451  eklendi. ---> Array size:  452  Array Length:  512
    452  eklendi. ---> Array size:  453  Array Length:  512
    453  eklendi. ---> Array size:  454  Array Length:  512
    454  eklendi. ---> Array size:  455  Array Length:  512
    455  eklendi. ---> Array size:  456  Array Length:  512
    456  eklendi. ---> Array size:  457  Array Length:  512
    457  eklendi. ---> Array size:  458  Array Length:  512
    458  eklendi. ---> Array size:  459  Array Length:  512
    459  eklendi. ---> Array size:  460  Array Length:  512
    460  eklendi. ---> Array size:  461  Array Length:  512
    461  eklendi. ---> Array size:  462  Array Length:  512
    462  eklendi. ---> Array size:  463  Array Length:  512
    463  eklendi. ---> Array size:  464  Array Length:  512
    464  eklendi. ---> Array size:  465  Array Length:  512
    465  eklendi. ---> Array size:  466  Array Length:  512
    466  eklendi. ---> Array size:  467  Array Length:  512
    467  eklendi. ---> Array size:  468  Array Length:  512
    468  eklendi. ---> Array size:  469  Array Length:  512
    469  eklendi. ---> Array size:  470  Array Length:  512
    470  eklendi. ---> Array size:  471  Array Length:  512
    471  eklendi. ---> Array size:  472  Array Length:  512
    472  eklendi. ---> Array size:  473  Array Length:  512
    473  eklendi. ---> Array size:  474  Array Length:  512
    474  eklendi. ---> Array size:  475  Array Length:  512
    475  eklendi. ---> Array size:  476  Array Length:  512
    476  eklendi. ---> Array size:  477  Array Length:  512
    477  eklendi. ---> Array size:  478  Array Length:  512
    478  eklendi. ---> Array size:  479  Array Length:  512
    479  eklendi. ---> Array size:  480  Array Length:  512
    480  eklendi. ---> Array size:  481  Array Length:  512
    481  eklendi. ---> Array size:  482  Array Length:  512
    482  eklendi. ---> Array size:  483  Array Length:  512
    483  eklendi. ---> Array size:  484  Array Length:  512
    484  eklendi. ---> Array size:  485  Array Length:  512
    485  eklendi. ---> Array size:  486  Array Length:  512
    486  eklendi. ---> Array size:  487  Array Length:  512
    487  eklendi. ---> Array size:  488  Array Length:  512
    488  eklendi. ---> Array size:  489  Array Length:  512
    489  eklendi. ---> Array size:  490  Array Length:  512
    490  eklendi. ---> Array size:  491  Array Length:  512
    491  eklendi. ---> Array size:  492  Array Length:  512
    492  eklendi. ---> Array size:  493  Array Length:  512
    493  eklendi. ---> Array size:  494  Array Length:  512
    494  eklendi. ---> Array size:  495  Array Length:  512
    495  eklendi. ---> Array size:  496  Array Length:  512
    496  eklendi. ---> Array size:  497  Array Length:  512
    497  eklendi. ---> Array size:  498  Array Length:  512
    498  eklendi. ---> Array size:  499  Array Length:  512
    499  eklendi. ---> Array size:  500  Array Length:  512
    500  eklendi. ---> Array size:  501  Array Length:  512
    501  eklendi. ---> Array size:  502  Array Length:  512
    502  eklendi. ---> Array size:  503  Array Length:  512
    503  eklendi. ---> Array size:  504  Array Length:  512
    504  eklendi. ---> Array size:  505  Array Length:  512
    505  eklendi. ---> Array size:  506  Array Length:  512
    506  eklendi. ---> Array size:  507  Array Length:  512
    507  eklendi. ---> Array size:  508  Array Length:  512
    508  eklendi. ---> Array size:  509  Array Length:  512
    509  eklendi. ---> Array size:  510  Array Length:  512
    510  eklendi. ---> Array size:  511  Array Length:  512
    511  eklendi. ---> Array size:  512  Array Length:  512
    
