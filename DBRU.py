'''
 DBRU Constructing a De Bruijn Graph

 Copyright (C) 2017 Greenweaves Software Pty Ltd

 This is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This software is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>

'''
import rosalind as r



if __name__=='__main__':
    A=[]
    with open('c:/Users/Weka/Downloads/rosalind_dbru(2).txt') as f:
        for line in f:
            A.append(line.strip())       
    _,E= r.dbru(A)
    for a,b in E:
        print('({0}, {1})'.format(a,b))
