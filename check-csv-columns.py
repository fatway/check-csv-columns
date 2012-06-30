#coding:utf-8
#check-csv-columns

__version__ = '0.1'


class CheckCsv(object):
    '''check csv files'''

    def __init__(self, csvfile):
        this.csvfile = csvfile
        this.line_col = {}   # mark line num & columns num
        this.col_count = {}  # mark columns num & num times

    def __csvreader(self):
        '''return a csvreader'''
        try:
            reader = csv.reader(open(self.cvsfile, 'rb'))
        except:
            reader = csv.reader(open(self.csvfile.decode('utf8'), 'rb'))
        return reader

    def __rnums(self, **kw1, **kw2):
        '''return list of columns num by the line count'''
        max_columns = 0
        max_columns_times = 0

        for col, times in kw2:
            if col > max_columns:
                max_columns = col
                max_columns_times = times

        for col, times in kw2:
            print 'columns: %s ' % col,
            print ',times: %s ' % times,

            if col == max_columns:
                print
            else:
                print ', in row: ',
                for nu, nu_col in kw1:
                    if nu_col == col:
                        print nu,
                print


    def checkcsv(self):
        '''markup the columns num and times in each line of csv file'''
        cur_col = -1

        for line in self.__csvreader():
            cols = len(line)
            self.line_col[line.line_num] = cols

            if cols == cur_col:
                self.col_count[cols] += 1
            else:
                if getattr(self.col_count, cols):
                    self.col_count[cols] += 1
                else:
                    self.col_count[cols] = 1

            cur_col = cols

        self.checkcsv(self.line_col, self.col_count)



if "__name__" == __main__:
    check = CheckCsv(raw_input('type in csv file path.'))
    check.checkcsv()

