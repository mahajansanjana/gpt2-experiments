library(tmasc)
data(erowid)

reports <- erowid[which(erowid[, 'substance'] %in% 
                        c('LSD', 
                          'Mushrooms', 
                          'DMT', 
                          'Ayahuasca')
                        )
                 , c('substance', 'text')]

write.csv(reports, 'reports.csv', row.names=FALSE)

