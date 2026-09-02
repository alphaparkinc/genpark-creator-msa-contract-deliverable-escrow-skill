class CreatorMsaContractDeliverableEscrowClient:
    def escrow_campaign_deliverables(self, creator_id='crt_772189', total_contract_value_usd=5000.00, agreed_deliverables=['1x YouTube Dedicated (8min+)', '2x Instagram Reels', '30-day Paid Ad Usage Rights']):
        return {
            'contract_escrow_id': 'msa_esc_8812',
            'creator_id': creator_id,
            'contract_status': 'FUNDS_ESCROWED_MILESTONE_ACTIVE',
            'escrowed_amount_usd': total_contract_value_usd,
            'milestones_pending_verification_count': len(agreed_deliverables),
            'automatic_rights_assignment_clause_included': True,
            'smart_contract_escrow_dossier_url': 'https://contracts.influencer.genpark.ai/msa/8812.json'
        }
