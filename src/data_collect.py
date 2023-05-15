import arxiv
import csv 

search = arxiv.Search(
  query = "blockchain",
  sort_by = arxiv.SortCriterion.SubmittedDate
)
FILEPATH = "data/"
header =  ['entry_id', 'updated', 'published', 'title', 'authors', 'summary', 'comment', 'journal_ref', 'doi', 'primary_category', 'categories', 'links',  'pdf_url'] 
data =[]
filename = "block_chain_test.csv"
filepath = FILEPATH + filename 

for result in search.results():
  row= [result.entry_id, result.updated, result.published, 
          result.title, result.authors, result.summary,result.comment, 
          result.journal_ref,result.doi,result.primary_category,result.categories, result.links,
          result.pdf_url]
  data.append(row) 
  # result.download_pdf()


with open( filepath, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(data)


# result.entry_id: A url http://arxiv.org/abs/{id}.
# result.updated: When the result was last updated.
# result.published: When the result was originally published.
# result.title: The title of the result.
# result.authors: The result's authors, as arxiv.Authors.
# result.summary: The result abstract.
# result.comment: The authors' comment if present.
# result.journal_ref: A journal reference if present.
# result.doi: A URL for the resolved DOI to an external resource if present.
# result.primary_category: The result's primary arXiv category. See arXiv: Category Taxonomy.
# result.categories: All of the result's categories. See arXiv: Category Taxonomy.
# result.links: Up to three URLs associated with this result, as arxiv.Links.
# result.pdf_url: A URL for the result's PDF if present. Note: this URL also appears among result.links.
