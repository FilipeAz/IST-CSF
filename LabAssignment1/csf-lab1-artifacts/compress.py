ó
&áYc           @   sä   d  d l  Z  d  d l Z d  d l Z d  d l m Z d   Z d   Z d   Z d   Z e	 d k rà e
 e  j  d k  r e e  j d	  n  e
 e  j  d
 k r¹ e e  j d
  d n d	 Z e e  j d e  j d e  n  d S(   iÿÿÿÿN(   t   Imagec         C   s§   g  } t  |   } g  t j d |  D] } t |  ^ q% } | g  |  D] } t |  ^ qG 7} x@ | D]8 } x/ t d d d  D] } | j | | ?d @ q Wqg W| S(   Nt   ii   iÿÿÿÿi   (   t   lent   structt   packt   ordt   ranget   append(   t   datat   vt   fSizet   bt   bytesR   (    (    s   csfsteg/csfsteghide.pyt	   decompose   s    +#c         C   s,   d | >} |  | M}  | r( |  | O}  n  |  S(   Ni   (    (   t   nR   t   xt   mask(    (    s   csfsteg/csfsteghide.pyt   set_bit   s
    
c         C   s  t  j |   } | j \ } } | j d  j   } d | | f GH| | d d d } d | GHt | d  } | j   }	 | j   d t |	  d	 GHt |	  }
 x! t |
  d
 rÈ |
 j	 d  q¨ Wt |
  d d	 } d | GH| | d k rd GHt
 j   n  t  j d | | f  } | j   } d } d } xAt |  D]3} x*t |  D]} | | k  rz| d } qXn  | j | | f  \ } } } } | t |
  k  rHt | d |
 |  } t | d |
 | d  } t | d |
 | d  } t | d |
 | d  } t | d |
 | d  } t | d |
 | d  } n  | d
 } | j | | f | | | | f  qXWqEW| j |  d d  d | GHd  S(   Nt   RGBAs#   [*] Input image size: %dx%d pixels.g      @i   i   s!   [*] Usable payload size: %.2f KB.t   rbs   [+] Payload size: %.3f KB g      @i   i    s#   [+] Embedded payload size: %.3f KB i   s    [-] Cannot embed. File too largei   i   i   i   s
   -stego.pngt   PNGs   [+] %s embedded successfully!(   R    t   opent   sizet   convertt   getdatat   readt   closeR   R   R   t   syst   exitt   newR   t   getpixelR   t   putpixelt   save(   t   imgFilet   payloadt   passwordt   imgt   widtht   heightt   convt   max_sizet   fR   R	   t   payload_sizet   steg_imgt   data_imgt   idxt   displacementt   ht   wt   rt   gR   t   a(    (    s   csfsteg/csfsteghide.pyt   embed#   sN    	
	
!
*c         C   s5   d GHd GHd GHd GHd |  GHd GHd GHt  j   d  S(   NsJ   Ciber Securanca Forense - Instituto Superior Tecnico / Universidade LisboasL   LSB steganography tool: hide files within least significant bits of images.
t    s   Usage:s)     %s <img_file> <payload_file> [password]s0     The password is optional and must be a number.(   R   R   (   t   progName(    (    s   csfsteg/csfsteghide.pyt   usageZ   s    	t   __main__i   i    i   i   i   (   R   R   t   numpyt   PILR    R   R   R4   R7   t   __name__R   t   argvt   intR#   (    (    (    s   csfsteg/csfsteghide.pyt   <module>   s   			7	
2