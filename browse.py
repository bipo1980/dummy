	def execute(self):
		if self.postresult: #-X
			self.__logger('Submitting results to testrail: [%s], [%s]' %(self.suitename, self.casetitle))
			self.__post_result()
			sys.exit(1)

		if self.addplan: # -A
			self.__logger("Adding Test Plan for Project id [%s] under Milestone id [%s]" %(self.projectid, self.milestoneid))
			self.__add_plan(self.projectid, self.milestoneid)	
			sys.exit(1)
