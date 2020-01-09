def main(env):
    fields = env['ir.model.fields'].search([])
    fields.filtered_domain([('model_id.name', '=like', 'a%')])
