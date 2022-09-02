# coding: utf-8
# Copyright (c) 2022 AtHomeDevelopers Team
#
# Author: Gaétan Suenge          <gaetansg26@gmail.com> 
#                                <athomedevelopers@gmail.com>
# JOIN US FOR OTHERS PROJECTS    <athomedevelopers@gmail.com>

""" Simple tools to draw tables in terminal """

from termcolor import colored


__ALL__ = ['center_text','classifier','draw']

VERSION = (0, 0, 1)

def center_text(text:str,spaces:int):
    """
    Center text.
    ===========
    Attributes
    ----------
        * text
        * spaces 
    Example
    -------
        >>> from brush import center_text
        >>> center_text('Hello, World!', 3)
    """
    if spaces%2 == 0:
        correct_spaces = ' '*(int(spaces/2))
        return '%s' %(correct_spaces+text+correct_spaces)
    else:
        correct_spaces_left = ' '*(int(spaces/2))
        correct_spaces_right = ' '*(spaces-correct_spaces_left.__len__())
        return '%s' %(correct_spaces_left+text+correct_spaces_right)


def classifier(values:list,index_for_classement:int,order:int):
    """
    Class a list
    ============
    Attributes
    ----------
        * values 
        * index_for_classement (1 or 2)
        * order
    Example
    -------
        >>> from brush import classifier
        >>> myValues = classifier(myValues,1,2)
    """
    correct_values, index = [], index_for_classement
    current = int()
    while values.__len__() > 0:
        for i in range(0,values.__len__()):
            if values[i][index] >= values[current][index]:
                current = i
        correct_values.append(values[current])
        values.pop(current)
        current = 0
    if order == 2:
        return correct_values
    elif order == 1:
        i = correct_values.__len__()-1
        while i >= 0:
            values.append(correct_values[i])
            i-=1
        return values   


def draw(headers:list,values:list,align_items='left',align_headers='left',add_separator_behind_items=False,add_ids=False,items_separator='-',colored_tables=False):
    """
    Draw
    =====
    Attributes
    ----------
        * headers
        * values 
        * align_items 
        * align_headers 
        * add_separator_behind_items 
        * add_ids
        * items_separator 
        * colored_tables (for Linux only)
    Example
    ------- 
        >>> from brush import draw
        >>> tables = draw(['players','team'],[['Lionnel Messi','Barcelona'],['Cristiano Ronaldo','Real Madrid']])
    """
    lines, spaces = list(), list()
    if add_ids:
        spaces_for_ids = str(values.__len__()).__len__()+2
    for i in headers:
        spaces.append(0)
        index = headers.index(i)
        if i.__len__() > spaces[index]:
            spaces[index] = i.__len__()
        for l in values:
            if str(l[index]).__len__() > spaces[index]:
                spaces[index] = str(l[index]).__len__()
    line = ''
    for i in range(0,headers.__len__()):
        space = ' '*(spaces[i]-headers[i].__len__())
        headers[i] = headers[i].upper()
        header = headers[i]
        if i == 0:
            if add_ids:
                line += (' '*spaces_for_ids)+' '
            if align_headers == 'right': line += '|%s|' %(space+header)
            elif align_headers == 'left': line += '|%s|' %(header+space)
            else: line += '|%s|' %(center_text(header,space.__len__()))
        else:
            if align_headers == 'right': line += '%s|' %(space+header)
            elif align_headers == 'left': line += '%s|' %(header+space)
            else: line += '%s|' %(center_text(header,space.__len__()))
    lines.append(line)
    lines.append('-'*line.__len__())
    counter = 1
    for l in values:
        line = ''
        for i in range(0,l.__len__()):
            space = ' '*(spaces[i]-str(l[i]).__len__())
            item = str(l[i])
            if i == 0:
                if add_ids:
                    line += '|%s' %(center_text(str(counter),spaces_for_ids-str(counter).__len__()))
                if align_items == 'right': line += '|%s|' %(space+item)
                elif align_items == 'left': line += '|%s|' %(item+space)
                else: line += '|%s|' %(center_text(item,space.__len__()))
            else:
                if align_items == 'right': line += '%s|' %(space+item)
                elif align_items == 'left': line += '%s|' %(item+space)
                else: line += '%s|' %(center_text(item,space.__len__()))
        lines.append(line)
        counter += 1
        if add_separator_behind_items:
            lines.append(items_separator*line.__len__())
    if colored_tables:
        lines[0] = colored(lines[0],'blue')
        lines[1] = colored(lines[1],'green')
        for i in range(2,lines.__len__()):
            lines[i] = lines[i].replace('|',colored('|','green'))
            lines[i] = lines[i].replace(items_separator,colored(items_separator,'green'))
    return lines